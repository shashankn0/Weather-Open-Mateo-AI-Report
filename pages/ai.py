import google.generativeai as genai
import os
#AIzaSyAaATNzmhk_gSmABukpNjux9EO9IQhwt5E -- AI KEY

export API_KEY=<AIzaSyAaATNzmhk_gSmABukpNjux9EO9IQhwt5E>
genai.configure(api_key=os.environ[AIzaSyAaATNzmhk_gSmABukpNjux9EO9IQhwt5E])
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
