# Đề bài 4:
# Dịch nguyên 1 file dài từ ngôn ngữ này sang ngôn ngữ khác.
#    1. Viết prompt để set giọng văn, v...v
#    2. Đọc từ file gốc, sau đó cắt ra thành từng phần để dịch vì LLM có context size có hạn
#    3. Sau khi dịch xong, gom kết quả lại, ghi vào file mới.


from dotenv import load_dotenv
import os
from openai import OpenAI
from PyPDF2 import PdfReader
import tiktoken

# def readContentFromFile(file_url):
#     """
#     Reads content from a PDF file and returns it as a string.
#     """
#     content = ""
#     try:
#         if os.path.exists(file_url) == True:
#             reader = PdfReader(file_url)
#             for page in reader.pages:
#                 content += page.extract_text()
#     except Exception as e:
#         print(f"Error reading file {file_url}: {e}")
#     return content

def read_file_in_chunks(file_path, chunk_size=1024):
    """
    Reads a file in chunks of specified size.
    :param file_path: Path to the file.
    :param chunk_size: Size of each chunk in bytes (default is 1024 bytes).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:  # Stop when no more content
                    break
                yield chunk  # Yield the chunk to process it
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

def read_pdf_in_chunks(file_path, chunk_size=1024):
    """
    Reads a PDF file and yields its content in chunks of specified size.
    :param file_path: Path to the PDF file.
    :param chunk_size: Size of each chunk in characters (default is 1024).
    """
    try:
        reader = PdfReader(file_path)
        content = ""

        # Extract text from all pages
        for page in reader.pages:
            content += page.extract_text()

        # Yield content in chunks
        for i in range(0, len(content), chunk_size):
            yield content[i:i + chunk_size]
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")


# def splitContentIntoChunks(content, max_tokens):
#     """
#     Splits content into chunks of approximately max_tokens using tiktoken.
#     """
#     encoding = tiktoken.get_encoding("cl100k_base")  # Use appropriate encoding for your model
#     tokens = encoding.encode(content)
#     chunks = []

#     for i in range(0, len(tokens), max_tokens):
#         chunk = encoding.decode(tokens[i:i + max_tokens])
#         chunks.append(chunk)

#     return chunks

def translateContent(content, api_url, api_key, model):
    translated_content = ""
    # Call API to translate content
    client = OpenAI(
        base_url=api_url, 
        api_key=api_key
    )

    # Prompt info
    llm_role="system"
    #llm_prompt="""Translate the following document from English to Vietnamese. The translation should be accurate, clear, and maintain the original meaning and tone. Preserve the original formatting as much as possible. Use formal language appropriate for the document."""
    llm_promt=os.getenv('TRANSLATE_PROMPT')
    llm_prompt = llm_prompt + "\n" + "===" + "\n" + content + "\n" + "==="

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
        temperature=0.7
    )

    translated_content = chat_completion.choices[0].message.content

    return translated_content

def writeContentToFile(translated_content, file_url):
    """
    Appends translated content into a text file.
    """
    try:
        with open(file_url, "a", encoding="utf-8") as file:
            file.write(translated_content + "\n")
    except Exception as e:
        print(f"Error writing to file {file_url}: {e}")


def main():
    # Load environment variables
    load_dotenv()
    BASE_URL = os.getenv('BASE_URL')
    API_KEY = os.getenv('API_KEY')
    MODEL = os.getenv('MODEL')
    context_size = 8192
    chunk_size = 1024
    source_file_url = 'file/climate_change_EN.pdf'
    dest_file_url = 'file/climate_change_VN.txt'

    # Read file in chunks, translate each chunk, and write to destination file
    for chunk in read_pdf_in_chunks(source_file_url, chunk_size):
        translated_content = translateContent(chunk, BASE_URL, API_KEY, MODEL)
        writeContentToFile(translated_content, dest_file_url)
    
if __name__ == "__main__":
    main()
