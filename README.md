# Summarizer App

A simple Flask application that utilizes the [Hugging Face Transformers](https://huggingface.co/transformers/) library to summarize text input using the BART model. This application is designed to provide quick and efficient text summarization for various types of content.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Summarization of text using the BART model.
- Easy-to-use API for text input.
- Containerized application using Docker for easy deployment.

## Technologies Used

- **Python**: Programming language used for the application.
- **Flask**: Web framework for building the web application.
- **Transformers**: Library for state-of-the-art NLP models from Hugging Face.
- **Docker**: Containerization technology for deployment.

## Getting Started

To get started with the Summarizer App, follow the instructions below.

### Prerequisites

- Python 3.7 or later
- Docker (for containerization)
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Humphery7/summarizer-app.git
   cd summarizer-app
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Run the application locally:**

   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8080/`.

### API Endpoints

- **GET /**: Summarizes the input text provided via the query parameter.

  - **Parameters:**
    - `input_text`: The text you want to summarize.
  - **Example Request:**

    ```
    http://127.0.0.1:8080/?input_text=Your text here.
    ```

  - **Response:**
    ```json
    {
      "summary": "This is the summarized text."
    }
    ```

## Deployment

This application can be deployed using Docker. Follow these steps to deploy:

1. **Build the Docker image:**

   ```bash
   docker build -t summarizer-app .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -d -p 8080:8080 summarizer-app
   ```

3. **Access the application:** Navigate to `http://127.0.0.1:8080/`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find a bug or have suggestions for improvements.

## License

This project is open sourced.
