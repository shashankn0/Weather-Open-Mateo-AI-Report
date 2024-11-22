import google.generativeai as genai
import os

model = genai.GenerativeModel("AIzaSyAaATNzmhk_gSmABukpNjux9EO9IQhwt5E") #this is the free model of google gemini
response = model.generate_content("Write a poem about how learning web development is fun!") #enter your prompt here!
print(response.text) #dont forget to print your response!
