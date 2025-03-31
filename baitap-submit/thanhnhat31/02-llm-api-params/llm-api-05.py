#Đề bài:
# Dùng bot để... giải bài tập lập trình. 
# Viết ứng dụng console cho phép bạn đưa câu hỏi vào, bot sẽ viết code Python/JavaScript. 
# Sau đó, viết code lưu đáp án vào file `final.py` và chạy thử. (Dùng Python sẽ dễ hơn JavaScript nhé!)

import os
from dotenv import load_dotenv
import openai

def getResponseFromLLM(api_url, api_key, model, prompt_content):
    """
    Sends a prompt to the LLM and returns the response.
    """  

    # Initialize OpenAI client
    client = openai.OpenAI(
        base_url=api_url, 
        api_key=api_key
    )

    # Prompt info
    llm_role="system"
    llm_prompt=prompt_content

    # Generate message
    input_messages = [
        {
            "role": llm_role,
            "content": llm_prompt
        },
    ]

    chat_completion = client.chat.completions.create(
        messages=input_messages,
        model=model,
        temperature=0.7,
        # max_tokens=1500,
        n=1,
    )

    response = chat_completion.choices[0].message.content
    return response
    

def save_code_to_file(code, filename):
    """
    Saves the generated code to a file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(code)
        print(f"Code saved to {filename}")
    except Exception as e:
        print("Error saving code: ", e)


def main():
    load_dotenv()
    BASE_URL = os.getenv('BASE_URL')
    API_KEY = os.getenv('API_KEY')
    MODEL = os.getenv('MODEL')
    system_prompt = os.getenv('GENERATE_CODE_PROMPT', "Please write a Python program to solve the following problem:")
    content_prompt = input("Enter your question: ")
    if(content_prompt.__len__() > 0):
        # Append user input into prompt
        #llm_prompt = llm_prompt + "\n" + "===" + "\n" + user_input + "\n" + "==="
        llm_prompt = f"""{system_prompt}
                        ===
                        {content_prompt}
                        ==="""

        response = getResponseFromLLM(BASE_URL,API_KEY, MODEL, llm_prompt)
        if response.__len__() > 0:
            # Insert response into file
            print("Generated code:\n", response)
            save_code_to_file(response, 'file\\final.py')


if __name__ == "__main__":
    main()