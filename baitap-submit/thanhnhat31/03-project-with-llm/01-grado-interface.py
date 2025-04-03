import gradio as gr

def greet(name, intensity):
    return f"Hello {name}, you are {intensity}!"

demo = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Slider(minimum=0, maximum=10, label="Intensity")
    ],
    outputs="text",
    title="Greeting App",
    description="A simple app to greet users with their name and intensity level."
)

demo.launch(share=True)