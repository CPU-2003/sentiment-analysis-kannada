
# Sentiment Analysis of Social Media Comments in Regional Languages: Kannada

This project deals with the analysis of sentiment of the kannada social media comments using the MuRIL model built by Google. 

We have built a model which takes in the kannada text and gives you the sentiment of it as positive or negative. 

The project has two different implementations.
1. API
2. Web App

The API is built using the FastAPI framework of python. This helps us to easily build a REST API, which by http/https calls gives us the result as expected.

The web app on the other hand is built using streamlit module which provides the structure of the web application. The web app uses the same API built before for providing the results. 




## Install the model

```bash
  nlp = pipeline(task='sentiment-analysis',model=googlw/muril-base-cased')
```
This will help you get the model downloaded and ready for implementation.


## Run the API

Runs the API on the local machine.

```bash
  uvicorn main:app --reload
```

Host the API

```bash
  https://localhost:8000/docs
```
This will provide you the Swagger ui of the API and the respective API calls, so that we can try out the API.

## Boot up the Web app

Start and run the web app
```bash
  streamlit run app.py
```

Enter the text and click the analyse sentiment button which gives you the sentiment as well as a befitting emoji.

Keep analysing the sentiments and write some positive comments. Adios amigos.....!


