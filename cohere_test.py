import cohere
import streamlit as st
import os

st.title("Cohere test")
co = cohere.Client(os.getenv('COHERE_KEY')) # This is your trial API key
response = co.generate(
  model='command',
  prompt='hello, its very hot, what will you suggest i do to get comfortable ? give me a list of 5 things in order of effectiveness and estimate the $ value\n',
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
st.write('Prediction: {}'.format(response.generations[0].text))
print('Prediction: {}'.format(response.generations[0].text))