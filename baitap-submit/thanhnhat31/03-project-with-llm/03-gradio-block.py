import gradio as gr

def greet(name: str) -> str:
    return f"Hello, {name}!"

with gr.Blocks() as demo:
    # Tự declare textbox đầu vào và textbox đầu ra
    with gr.Row():
        name_input = gr.Textbox(label="Name", placeholder="Enter your name")
        greeting_output = gr.Textbox(label="Greeting", placeholder="Your greeting will appear here")

    # Tạo button, goi hàm greet khi nhấn button
    greet_button = gr.Button("Greet")
    greet_button.click(greet, inputs=name_input, outputs=greeting_output)

demo.launch(share=True)