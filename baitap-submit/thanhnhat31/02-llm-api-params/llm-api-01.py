#1. Viết một ứng dụng console đơn giản, người dùng gõ câu hỏi vào console, bot trả lời và in ra. Có thể dùng `stream` hoặc `non-stream`.
from dotenv import load_dotenv
import os
from openai import OpenAI

def main():
    # Load environment variables
    load_dotenv()
    BASE_URL = os.getenv('BASE_URL')
    API_KEY = os.getenv('API_KEY')
    MODEL = os.getenv('MODEL')
    stop_chat = False

    # Create OpenAI client
    client = OpenAI(
        base_url=BASE_URL, 
        api_key=API_KEY
    )

    # Generate message
    input_messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
    ]

    while not stop_chat:
        # Get user input
        user_input = input("Enter your message: ")
        if(user_input.__len__() > 0):
            if(user_input == "exit" or user_input == "quit"):
                stop_chat = True
            else:
                input_messages.append(
                    {
                        "role": "user",
                        "content": user_input
                    }
                )

                # Call API
                stream = client.chat.completions.create(
                    messages=input_messages,
                    model=MODEL,
                    stream=True
                )

                # Print response
                for chunk in stream:
                    print(chunk.choices[0].delta.content or "", end="")

if __name__ == "__main__":
    main()
    