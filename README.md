# Animated Face Generator
An Animated Face Generator built using Python, FastAPI, and a GAN model based on a modified ResNet-18 architecture. This project provides a backend API that generates realistic animated face outputs using a pre-trained face generation model.
The system is designed for scalability, modularity, and easy deployment, making it suitable for experimentation, demos, or integration into frontend applications.

## Features
* Face generation using a GAN with ResNet-18 backbone
* Fast and scalable FastAPI backend
* Uvicorn ASGI server for high-performance inference
* RESTful API for face generation requests
* Modular project structure for easy extension
* Pre-trained model loading for quick startup

## Replicate The Code
pip install -r requirements.txt

Once running, the API will be available at:
http://localhost:8000

## Interactive API documentation:
Swagger UI: /docs
ReDoc: /redoc

## Generate Animated Face

### Endpoint
GET /generate?n={number of images to generate}

### Response
Generated animated face data list of base64 encoded images

## Frontend Integration

The frontend is already deployed at https://anyani.netlify.app and communicates with this backend via REST APIs

CORS is enabled for frontend domain access

Responses are structured for easy frontend consumption

