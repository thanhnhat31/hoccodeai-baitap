from diffusers import EulerDiscreteScheduler, DDIMScheduler, DPMSolverMultistepScheduler, DiffusionPipeline

prompt = "girl with puppy ears"
steps = 30

pipeline = DiffusionPipeline.from_pretrained("stablediffusionapi/anything-v5", use_safetensors=True, safety_checker=None, requre_safety_checker=False)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipeline.to(device)
pipeline.scheduler = EulerDiscreteScheduler.from_config(pipeline.scheduler.config)

# Sử dụng cùng một prompt với 3 scheduler khác nhau mới
image = pipeline(prompt, num_inference_steps=steps).images[0]
image.show()

pipeline.scheduler = DDIMScheduler.from_config(pipeline.scheduler.config)
image = pipeline(prompt, num_inference_steps=steps).images[0]
image.show()

pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)
image = pipeline(prompt, num_inference_steps=steps).images[0]


image.show()