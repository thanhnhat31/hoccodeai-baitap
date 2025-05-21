# # Bài tập

# 1. Dùng chunking để làm bot trả lời tiểu sử người nổi tiếng, anime v...v
#   - <https://en.wikipedia.org/wiki/S%C6%A1n_T%C3%B9ng_M-TP>
#   - <https://en.wikipedia.org/wiki/Jujutsu_Kaisen>


import os
import pprint
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
from wikipediaapi import Wikipedia
from openai import OpenAI

def collection_exists(client, collection_name):
    collections = client.list_collections()
    return any(col.name == collection_name for col in collections)

def create_collection(wikipedia_url:str, collection_name: str, client):
    embedding_function = embedding_functions.DefaultEmbeddingFunction()
    collection = client.create_collection(name=collection_name, embedding_function=embedding_function)

    # Sử dụng wikipediaapi để lấy dữ liệu từ https://en.wikipedia.org/wiki/Jujutsu_Kaisen
    wiki = Wikipedia(f'HocCodeAI/0.0 ({wikipedia_url})', 'en')
    doc = wiki.page("Jujutsu Kaisen").text

    # In dữ liệu ra
    print(doc)

    # Chia nhỏ văn bản một cách đơn giản
    paragraphs = doc.split('\n\n')

    # Lưu trữ các đoạn văn bản trong collection
    for index, paragraph in enumerate(paragraphs):
        collection.add(documents=[paragraph], ids=[str(index)])

    return collection

def execute_query(question:str, collection):
    q = collection.query(query_texts=[question], n_results=3)
    results = q['documents'][0]
    print(results)
    return results


def get_answer(client: OpenAI, model:str, question:str, collection):
    CONTEXT = execute_query(question, collection)

    # Xây dựng prompt, đưa dữ liệu vừa truy xuất vào làm ngữ cảnh trong biến `CONTEXT`
    prompt = f"""
    Use the following CONTEXT to answer the QUESTION at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Use an unbiased and journalistic tone.

    CONTEXT: {CONTEXT}

    QUESTION: {question}
    """

    # Sử dụng RAG để trả lời câu hỏi, trong biến `prompt` đã có ngữ cảnh
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    query_result = response.choices[0].message.content
    return query_result


# Xử lý chính
def main():
    # Load environment variables from .env file
    load_dotenv()
    BASE_URL = os.getenv("BASE_URL")
    #API_KEY = os.getenv("API_KEY")
    API_KEY = os.getenv("TOGETHER_API_KEY")
    MODEL = os.getenv("MODEL")

    if not BASE_URL or not API_KEY or not MODEL:
        raise ValueError("LLM parameters are not set. Please check your enviroment.")

    OpenAI_client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY,
    )

    if OpenAI_client is None:
        raise ValueError("Client is not initialized. Please check your API key and base URL.")

    # Check Chromadb connection and create collection 
    wikipedia_url = "https://en.wikipedia.org/wiki/Jujutsu_Kaisen"
    COLLECTION_NAME = "Jujutsu_Kaisen"

    # Ở đây, ta dùng `PersistentClient` để lưu trữ dữ liệu trong một file trong thư mục `./data`.
    client = chromadb.PersistentClient(path="./data/chromadb")
    client.heartbeat()  

    if collection_exists(client, COLLECTION_NAME):
        collection = client.get_collection(COLLECTION_NAME)
    else:
        collection = create_collection(wikipedia_url=wikipedia_url, collection_name=COLLECTION_NAME, client=client)

    while True:
        # Get input from userpy 
        question = input("Bạn có câu hỏi gì không? ")
        if question.lower() in ['quit', 'close', 'exit']:
            break

        get_answer(question=question, client=OpenAI_client, model=MODEL, collection=collection)

if __name__ == "__main__":
    main()
