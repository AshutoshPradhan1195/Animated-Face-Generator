from glob import glob
import torch
import matplotlib.pyplot as plt
from app.Services.Generator import Generator
import io
from PIL import Image
import numpy as np

latent_size = 128
stats = ((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
model = Generator(latent_size)
state_dict = torch.load("app/Services/GAN_lr0.0008_epoch_100", weights_only=True, map_location=torch.device('cpu'))
# Load the state dictionary into the model
model.load_state_dict(state_dict)

def denormalize(image):
    return image * stats[1][0] + stats[0][0]

def generate_image(generator,n = 10):
    with torch.no_grad():
        latent_images = torch.randn(n, latent_size, 1, 1)
        images = generator(latent_images)
        return images




def tensor_to_pil(img):
    img = denormalize(img)
    img = img.clamp(0, 1)
    img = (img * 255).byte()
    img = img.permute(1, 2, 0).cpu().numpy()
    return Image.fromarray(img)

def generateImages(n=1):
    images = generate_image(generator=model, n=n)
    pil_images = [tensor_to_pil(img) for img in images]
    return pil_images

def generateImages(n=10):

    model.eval()

    images = generate_image(generator=model, n=n)
    pil_images = [tensor_to_pil(img) for img in images]
    return pil_images
