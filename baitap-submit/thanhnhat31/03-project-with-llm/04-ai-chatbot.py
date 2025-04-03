import os
import random
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI


load_dotenv()
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def chat_logic(message, chat_history):
    # Chuyển đổi tin nhắn thành định dạng mà Gemini yêu cầu
    messages = []
    for user_message, bot_message in chat_history:
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": bot_message})
    
    # Thêm tin nhắn mới của user vào cuối danh sách
    messages.append({"role": "user", "content": message})

    # Thêm tin nhắn "Đang chờ..." vào lịch sử chat và hiển thị
    chat_history.append([message, "Waiting..."])
    yield "", chat_history

    # Gọi API của Gemini để lấy phản hồi
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=MODEL,
        temperature=0.7,
        max_tokens=-1,
        stream=True
    )

     # Xóa tin nhắn "Đang chờ..."
    chat_history[-1][1] = "" 
    # Hiển thị phản hồi từ Gemini, stream dần dần thay vì chờ tất cả kết quả mới trả lời
    for chunk in chat_completion:
        delta = chunk.choices[0].delta.content or ""

        # Update tin nhắn cuối cùng trong lịch sử chat
        chat_history[-1][1] += delta
        # Hàm yield trả về kết quả dạng generator, giúp Gradio hiển thị kết quả dần dần
        yield "", chat_history

    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("# Chatbot bằng Gemini")
    message = gr.Textbox(label="Nhập câu hỏi của bạn", placeholder="Hãy hỏi tôi bất cứ điều gì!")
    chatbot = gr.Chatbot(label="Chatbot siêu thông minh", height=600)

    # Khi user nhập tin nhắn, gọi hàm chat_logic
    message.submit(chat_logic, inputs=[message, chatbot], outputs=[message, chatbot])

demo.launch()