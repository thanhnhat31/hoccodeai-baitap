import gradio as gr
import torch
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the BLIP model and processor
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base", torch_dtype=torch.float16).to(device)

# Define the function to generate captions
# The function takes a raw image as input and returns a caption
# The function uses the BLIP model to process the image and generate a caption
def generate_caption(raw_image: Image):
    inputs = processor(raw_image, return_tensors="pt").to(device, torch.float16)
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

image_url = 'https://pbs.twimg.com/media/GQcYASfX0AAUezI?format=jpg&name=medium'
# Download the image from the URL and open it using PIL
# The image is loaded from a URL and passed to the generate_caption function    
image = Image.open(requests.get(image_url, stream=True).raw)
caption = generate_caption(image)
print(f"Caption: {caption}")


# Input đầu vào là một ảnh
image = gr.Image(label="Input Image")

# Output đầu ra là một caption
caption = gr.Textbox(label="Caption")

# Create a Gradio interface with the function, inputs, and outputs
# The interface allows users to upload an image and get a caption in return
gr.Interface(fn=generate_caption, 
             inputs=image, 
             outputs=caption, 
             title="Image Captioning with BLIP", 
             description="Generate captions for images using BLIP model.").launch(share=True)