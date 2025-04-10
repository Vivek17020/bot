import streamlit as st
import pandas as pd
import json
from nltk.corpus import wordnet as wn

def load_data():
    try:
        df = pd.read_csv('Medical_dataset/Training.csv')
        return df
    except FileNotFoundError:
        st.error("Dataset not found! Make sure 'Training.csv' is available.")
        return None

def write_json(new_data, filename='DATA.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["users"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def chatbot_response(user_input):
    synonyms = set()
    for syn in wn.synsets(user_input):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return f"I found these synonyms: {', '.join(synonyms)}" if synonyms else "I couldn't find synonyms."

# Streamlit UI
st.title("Medical Chatbot")

df = load_data()
if df is not None:
    st.write("Dataset Loaded Successfully!")

user_input = st.text_input("Ask me something:")
if st.button("Send"):
    response = chatbot_response(user_input)
    st.write("Chatbot:", response)
