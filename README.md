# AFRISCORE
This project is a FastAPI application that predicts credit qualification for customers based on certain features. The application is containerized using Docker and is available on Docker Hub.

A detailed proposal to this project can be found [here;](https://docs.google.com/document/d/1XpOUKyt2DH6wQ9Pfeq8w31DLfAjhRlRRcslEcjtVSMM/edit?usp=sharing)

## Afriscore Lean canvas
A lean canvas that defines the business/economic relevance of Afriscore can be found [here;](https://docs.google.com/presentation/d/1CuriQnHya5FZHXnSRDSemWuFRwSQiF11ElNvd3cSdUw/edit?usp=sharing)

## Features
- FastAPI for creating the web application
- Docker for containerization and easy deployment
- Predictive model for credit qualification
## Setup

### Prerequisites
* Docker installed on your machine. If you don't have Docker installed, you can download it from [here];(# My FastAPI Project

This project is a FastAPI application that predicts credit qualification for customers based on certain features. The application is containerized using Docker and is available on Docker Hub.

## Features

- FastAPI for creating the web application
- Docker for containerization and easy deployment
- Predictive model for credit qualification

## Setup

### Prerequisites

- Docker installed on your machine. If you don't have Docker installed, you can download it from [here](https://www.docker.com/products/docker-desktop).

### Steps

1. **Pull the Docker image from Docker Hub:**

   Open your terminal and run the following command to pull the Docker image:

   ```bash
   docker pull martinalu/myrepo:latest
   ```

2. **Run the Docker container:**

   After pulling the image, you can run a container with the following command:

   ```bash
   docker run -p 8000:8000 martinalu/myrepo:latest
   ```

   This command maps port 8000 inside the Docker container to port 8000 on your local machine.

3. **Access the FastAPI application:**

   Once the Docker container is running, you can access the FastAPI application at `http://localhost:8000/docs`.

## Usage

The application exposes a POST endpoint at `/predict` that accepts JSON data in the following format:

```json
{
  "age": 30,
  "month": "jan",
  "day": 15,
  "balance": 2000,
  "duration": 300,
  "pdays": 5
}
```

You can use a tool like `curl` or Postman to send a POST request to `http://localhost:8000/predict` with the above JSON data. Additionally, FastAPI provides an interactive Swagger UI that you can use to send requests to the model. You can access this UI at `http://localhost:8000/docs`.

## Contribution/Further Development

This FastAPI application provides a simple and efficient way to predict credit qualification for customers. However, there are several ways this project could be extended:

- **Improve the Model:** The current model is a simple example. It could be improved by using more sophisticated machine learning techniques or by tuning the hyperparameters.
- **Add More Features:** The model currently uses a limited set of features. Adding more features could improve the accuracy of the predictions.
- **Automate Retraining:** The model could be retrained automatically on a regular basis or when new data becomes available.
- **Add More Endpoints:** The application currently has a single endpoint. More endpoints could be added to provide additional functionality.

Contributions to this project are welcome. If you have an idea for an improvement, please open an issue to discuss it before making any changes. Once the idea has been approved, you can make the changes and open a pull request.