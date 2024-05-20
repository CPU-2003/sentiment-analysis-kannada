import streamlit as st
import requests
import json
from main import modell
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Define the URL of the FastAPI endpoint
API_URL = 'http://localhost:8000/predict/'


# Streamlit UI components
st.title('Sentiment Analysis App')

# Text input box for user input
user_input = st.text_area('Enter text:', '')

payload = {"text": str(user_input)}

# Button to trigger sentiment analysis
if st.button('Analyze Sentiment'):
    # Check if user has entered text
    if str(user_input) == "":
        st.write("no input")
    if user_input:
        
        
        # Call API and get sentiment analysis results
        result = requests.post(API_URL, data= json.dumps(payload))
        response = json.loads(result.text)
        # st.write(f"sentiment:",response['sentiment'])

        if response['sentiment'] in ["positive","very positive"]:
            st.markdown("⭐️✨🎉 Positive 🎉✨⭐️")
            st.image("images\positive.jpg")
        else:
            st.markdown("😞 Negetive 😞")
            st.image('images\depressed.jpg')
            
        