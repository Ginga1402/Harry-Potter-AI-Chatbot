### Create a custom Question-Answer (QA) chatbot using your own input data.


# Harry Potter AI-Based Chatbot

# Wizard Whispers Chatting in the Potterverse

Welcome to the Harry Potter AI-Based Chatbot repository! This project allows you to create a custom Question-Answer (QA) chatbot using your own input data. In this case, we have implemented a Harry Potter-themed chatbot, leveraging the power of natural language processing to provide an interactive and immersive experience for users.


## Table of Contents
Overview

Getting Started

Customizing the Chatbot

Usage

Example

Contributing

License




## Overview
This repository contains the code for a customizable QA chatbot that has been trained on Harry Potter-related data. The chatbot is powered by natural language processing techniques, allowing it to understand and respond to user queries about the Harry Potter universe.

## Tech Stack Used
The following technologies and libraries were used in the development of this chatbot:

Python: Programming language used for the implementation.

Langchain: LangChain is a framework designed to simplify the creation of applications using large language models.

Chroma DB: Chroma DB is an open-source vector store used for storing and retrieving vector embeddings.

Ctransformers: The C Transformers library provides Python bindings for GGML models.

Model Used: Llama 2 is a family of pre-trained and fine-tuned large language models (LLMs) released by Meta AI in 2023. Released free of charge for research and commercial use, Llama 2 AI models are capable of a variety of natural language processing (NLP) tasks, from text generation to programming code. 

## Getting Started
To get started with the Harry Potter AI-Based Chatbot, follow these steps:

#### 1. Clone the repository to your local machine:

git clone https://github.com/Ginga1402/harry-potter-chatbot.git

#### 2. Install the required dependencies:

pip install -r requirements.txt

#### 3. Run the chatbot application:
python chatbot.py

Interact with the chatbot by entering your Harry Potter-related questions.

## Customizing the Chatbot
If you want to customize the chatbot for a different theme or use case, you can update the input data and retrain the model. Follow these steps:

1. Replace the existing data in the data folder with your own dataset. Ensure that the data is in a suitable question-answer format.

2. Modify the training configuration in the config.json file to match your dataset and preferences.

3. Run the ingestion script to make embeddings for the chatbot:

python ingestion.py

Once the embedding is ready, you can run the chatbot again with the updated model.

## Usage
The chatbot uses a simple command-line interface. Enter your questions, and the chatbot will provide relevant answers .

## Example
Here's an example interaction with the Harry Potter AI-Based Chatbot:

![image](https://github.com/Ginga1402/Harry-Potter-AI-Chatbot/assets/130181481/79d708a7-e1bc-4968-80b5-947124d5edb5)


## Contributing
Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Happy chatting in the magical world of Harry Potter! 🧙🏻‍♂️✨
