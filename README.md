# Text Summarization Web App

link :https://quicksummary-ai.onrender.com
This project implements a web application for text summarization using Flask and Spacy.

## Overview

The application allows users to input a piece of text and get a summarized version of it based on a specified percentage of the original text length. It utilizes the `en_core_web_sm` model from Spacy for natural language processing.

## Libraries Used

- Flask: Used for building the web application and handling HTTP requests.
- Spacy: Utilized for natural language processing tasks, including text tokenization and summarization.
- Gunicorn: Used as a WSGI server for deploying the Flask application.
- Pickle: Used for serializing and deserializing Python objects, essential for saving the trained model.

## Skills Learned

- Implementing a web application using Flask.
- Integrating a machine learning model (Spacy) for text processing.
- Serializing and deserializing Python objects for model persistence.
- Deploying a Python web application using Gunicorn.

## Files

- `app.py`: Flask application setup and routes.
- `text.py`: Text summarization logic using Spacy.
- `requirements.txt`: List of Python dependencies.
- `download_spacy_model.py`: Script to download and configure Spacy model.

