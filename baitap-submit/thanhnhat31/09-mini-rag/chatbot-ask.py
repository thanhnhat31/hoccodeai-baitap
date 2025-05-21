# # Bài tập

# 2. Thay vì hardcode `doc = wiki.page('Hayao_Miyazaki').text`, sử dụng function calling để:
#   - Lấy thông tin cần tìm từ câu hỏi
#   - Dùng `wiki.page` để lấy thông tin về
#   - Sử dụng RAG để có kết quả trả lời đúng.


import json
import os
import pprint
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
from openai import OpenAI
import wikipedia
import inspect
from pydantic import TypeAdapter

def collection_exists(collection_name, rag_client) -> bool:
    collections = rag_client.list_collections()
    return any(col.name == collection_name for col in collections)

def create_collection(collection_name: str, wiki_page: wikipedia.page, rag_client):
    collection = None
    try:
        embedding_function = embedding_functions.DefaultEmbeddingFunction()
        collection = rag_client.create_collection(name=collection_name, embedding_function=embedding_function)

        doc = wiki_page.content

        # # Chia nhỏ văn bản một cách đơn giản
        paragraphs = doc.split('\n\n')

        # # Lưu trữ các đoạn văn bản trong collection
        for index, paragraph in enumerate(paragraphs):
            collection.add(documents=[paragraph], ids=[str(index)])
    except Exception as ex:
        print(f"Error: {ex}")

    return collection

def rag_query(question:str, collection):
    q = collection.query(query_texts=[question], n_results=3)
    results = q['documents'][0]
    print(f"RAG Query Result: {results}")
    return results


def find_subject(message: str, openai_client, model) -> str:
    prompt = f"""You are an AI assistant tasked with identifying the central theme of the provided message. Please analyze the message and return a concise theme title.
                    Instructions for Theme Identification:
                    - Understand the Core Content: Read the message thoroughly to grasp its main subject matter or the primary issue being addressed.
                    - Identify the Central Topic: Pinpoint the most important concept, question, or idea that the message revolves around.
                    - Formulate a Theme Title:
                        + Express the theme as a brief, descriptive title or a short noun phrase.
                        + The title should be concise and directly reflect the core topic.
                        + Focus on what the message is about, rather than a full summary of its arguments or details.
                    - Be Objective: The theme title should be neutral and accurately represent the subject.
                    - Single Focus: Aim to identify the single most dominant theme.
                    - Do not return any information other than the theme title.
                    Message to Analyze:
                    {{{message}}}"""

    messages = [
        {
            "role": "system","content": prompt,
        },
    ]

    # Gọi LLM để lấy phản hồi
    try:
        chat_completion = openai_client.chat.completions.create(
            messages=messages,
            model=model,
        )

        subject = chat_completion.choices[0].message.content
        print(f"Theme: {subject}")
        return subject
    except Exception  as ex:
        print(f"Error: {ex}")
    

def search_wikipedia(question: str) -> str:
    """
    Find in Wikipedia informations related to question from user. After getting data, use this data to answer the specified question
    :param question: subject that needs to find in wikipedia, e.g., 'what is large language model'
    :output: An answer of target question
    """

    global openai_client, model, rag_client

    results = ""
    subject = find_subject(question, openai_client, model)
    if subject:
        try:
            search_results = wikipedia.search(subject)
            print("Search results:", search_results) 
        except Exception  as ex:
            print(f"Error: {ex}")

        if search_results:
            wiki_page = wikipedia.page(search_results[0])
            print(f"Wiki Page: {wiki_page}")
            # print("Title:", page.title)
            # print("Summary:", page.summary)
            # print("Full text:", page.content)

            # Get collection
            collection_name =  subject.replace(" ","_")
            if collection_exists(collection_name=collection_name, rag_client=rag_client):
                collection = rag_client.get_collection(collection_name)
            else:
                collection = create_collection(collection_name=collection_name, wiki_page=wiki_page, rag_client=rag_client)

            if collection:
                results = rag_query(question, collection)
    else:
        print("No subject found.")
    
    return results

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_wikipedia",
            "description": inspect.getdoc(search_wikipedia),
            "parameters": TypeAdapter(search_wikipedia).json_schema(),
        },
    },
]

def get_completion(messages):
    global openai_client, model

    response = openai_client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        temperature=0
    )

    return response
    

def get_answer(question: str):
    global openai_client, model

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant. Use the supplied tools to answer the question from user."},
        {"role": "user", "content": question}
    ]

    response = get_completion(messages)
    first_choice = response.choices[0]
    print(f"First choice (1): {first_choice}")

    finish_reason = first_choice.finish_reason
    print(f"Finish reason (1): {finish_reason}")

    FUNCTION_MAP = {
        "search_wikipedia": search_wikipedia
    }

    while finish_reason != "stop":
        tool_call = first_choice.message.tool_calls[0]

        tool_call_function = tool_call.function
        tool_call_arguments = json.loads(tool_call_function.arguments)

        tool_function = FUNCTION_MAP[tool_call_function.name]
        result = tool_function(**tool_call_arguments)

        print(f"Call {tool_call_function.name} with params {tool_call_function.arguments}. Result: {result}.")

        messages.append(first_choice.message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call_function.name,
            "content": json.dumps({"result": result})
        })

        print(f"Message: {messages}")

        # Chờ kết quả từ LLM
        response = get_completion(messages)
        first_choice = response.choices[0]
        print(f"First choice (2): {first_choice}")

        finish_reason = first_choice.finish_reason
        print(f"Finish reason (2): {finish_reason}")

    # In ra kết quả sau khi đã thoát khỏi vòng lặp
    print(f"BOT RESULT: {first_choice.message.content}")

# Xử lý chính
openai_client = None
model = None
rag_client = None

def main():
    global openai_client, model, rag_client
    # Load environment variables from .env file
    load_dotenv()
    BASE_URL = os.getenv("BASE_URL")
    #API_KEY = os.getenv("API_KEY")
    API_KEY = os.getenv("TOGETHER_API_KEY")
    model = os.getenv("MODEL")

    if not BASE_URL or not API_KEY or not model:
        raise ValueError("LLM parameters are not set. Please check your enviroment.")

    openai_client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY,
    )

    if openai_client is None:
        raise ValueError("Client is not initialized. Please check your API key and base URL.")

    # Check Chromadb connection and create collection 
    # Ở đây, ta dùng `PersistentClient` để lưu trữ dữ liệu trong một file trong thư mục `./data`.
    rag_client = chromadb.PersistentClient(path="./data/chromadb")
    rag_client.heartbeat()  

    if rag_client is None:
        raise ValueError("RAG Client is not initialized.")

    while True:
        # Get input from userpy 
        question = input("Bạn có câu hỏi gì không? ")
        if question.lower() in ['quit', 'close', 'exit']:
            break

        # get_answer(question=question, client=OpenAI_client, model=MODEL, collection=collection)
        if len(question) != 0:
            get_answer(question=question)

if __name__ == "__main__":
    main()
