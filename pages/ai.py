import google.generativeai as genai
import os
#AIzaSyAaATNzmhk_gSmABukpNjux9EO9IQhwt5E -- AI KEY

curl \
  -H "Content-Type: application/json" \
  -d "{\"contents\":[{\"parts\":[{\"text\":\"Explain how AI works\"}]}]}" \
  -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyAaATNzmhk_gSmABukpNjux9EO9IQhwt5E"

model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
response = model.generate_content("Write a poem about how learning web development is fun!") #enter your prompt here!
print(response.text) #dont forget to print your response!
