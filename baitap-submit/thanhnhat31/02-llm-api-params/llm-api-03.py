# Đề bài:
#3. Tóm tắt website. Dán link website vào console, bot sẽ tóm tắt lại nội dung của website đó.
#
#   1. Người dùng dán link <https://tuoitre.vn/cac-nha-khoa-hoc-nga-bao-tu-manh-nhat-20-nam-sap-do-bo-trai-dat-2024051020334196.htm> vào console
#   2. Sử dụng `requests` để lấy nội dung website.
#   3. Dùng thư viện `beautifulsoup4` để parse HTML. (Bạn có thể hardcode lấy thông tin từ div có id là `main-detail` ở vnexpress)
#   4. Bạn cũng có thể thay bước 2-3 bằng cách dùng <https://jina.ai/reader/>, thên `r.jina.ai` để lấy nội dung website.
#   5. Viết prompt và gửi nội dung đã parse lên API để tóm tắt. (Xem lại bài prompt engineering nha!)
#


from dotenv import load_dotenv
import os
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

def getContentFromUrl(url):
    content = ""
    try:
        # Fetch the website content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract specific content (e.g., content inside a div with id="main-detail")
        content = soup.find(id="main-detail").get_text()
        return content
    except Exception as e:      
        print("Error: ", e)
        return None

    

def main():
    # Load environment variables
    load_dotenv()
    BASE_URL = os.getenv('BASE_URL')
    API_KEY = os.getenv('API_KEY')
    MODEL = os.getenv('MODEL')
    stop_chat = False
    content = ""

    # Prompt info
    llm_role="system"
    llm_promt = """Please summarize the following article while focusing on the key points and important details. Your summary should be concise yet informative, capturing the essence of the content. As you summarize, try to maintain a positive tone and inject a bit of humor where appropriate, without detracting from the core message. Write the summary in Vietnamese.
                When generating the summary, consider the following:
                - Identify and include the main ideas, central themes, and crucial plot points
                - Omit unnecessary details or tangential information that doesn't contribute to the overall understanding
                - Use clear and concise language to convey the summary effectively
                - Maintain a positive spin on the content, highlighting uplifting or amusing aspects where possible
                - If suitable, incorporate a touch of wit or humor to make the summary more engaging"""
    



    # Get user input
    url = input("Enter the website link: ")
    if(url.__len__() > 0):
        content = getContentFromUrl(url)
    
    # Append content into prompt
    llm_promt = llm_promt + "\n" + content

    #Create OpenAI client
    client = OpenAI(
        base_url=BASE_URL, 
        api_key=API_KEY
    )

    # Generate message
    input_messages = [
        {
            "role": llm_role,
            "content": llm_promt
        },
    ]

    chat_completion = client.chat.completions.create(
        messages=input_messages,
        model=MODEL,
        #max_tokens=1028,
        temperature=0.7
    )

    # Print response
    print(chat_completion.choices[0].message.content)



if __name__ == "__main__":
    main()