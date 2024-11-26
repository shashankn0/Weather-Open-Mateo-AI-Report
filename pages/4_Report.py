simport streamlit as st
import requests
import google.generativeai as genai
import os
cityFound = False
st.title("Today's Weather in your City")

    
state = st.selectbox("State",['Alabama', 'Alaska', 'Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montanta','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'], placeholder = "State")

city = st.text_input("City")
oldCity = city[:]
if ' ' in city:
    fCity = ''
    city = city.split(" ")
    for item in city:
        fCity += item + "+"
    city = fCity[:-1]
    
st.write("")
st.write("")

try:
    api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&state={}'.format(city,state)
    response = requests.get(api_url + city + state, headers = {'X-Api-Key': 'EQ41HwpJwt7hYy2gHk7SfQ==vOltY334CaIzpR6u'})


    data = response.json()
    if response.status_code==200:
        lat = ''
        long = ''
        for item in data:
            if item['state']==state:
                lat = item['latitude']
                long = item['longitude']
    
    

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": long,
            "forecast_days": 1,
            "daily": "apparent_temperature_max,apparent_temperature_min,precipitation_probability_mean"
            }
        response = requests.get(url, params = params)

    if response.status_code == 200:
        data = response.json()

        time = str(data["daily"]["time"])
        temp_max = data["daily"]["apparent_temperature_max"]
        temp_min = data["daily"]["apparent_temperature_min"]
        precip_prob = data["daily"]["precipitation_probability_mean"]



        genai.configure(api_key = 'AIzaSyAC-2udy2vUhyuee4Dw4fk8BCNBfMxm_gI')

        st.subheader(f"Today's Report in {oldCity}, {state}:")
    
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Generate a weather report for the date,{time}, with a maximum temperature of {temp_max} and a minimum temperature of {temp_min} and a {precip_prob} chance of rain.")

        st.write(response.text)
        cityFound = True


except:
    st.subheader("Your city cannot be found.")
    cityFound = False

    
if cityFound==True:
     st.subheader("What should you wear today??")
     st.write("Ask about what your should wear or whether the outfit you have planned will fit with today's conditions!")
     if "conversation_history" not in st.session_state:
              st.session_state.conversation_history = []
     if "input_text" not in st.session_state:
              st.session_state.input_text = ""
            
     def submit():
         if st.session_state.input_text:
              model = genai.GenerativeModel("gemini-1.5-flash")
              response2 = model.generate_content(f"Answer the following question so the asker can figure out what to wear today, {st.session_state.input_text}, given the weather conditions of today: maximum temperature={temp_max}, minimum temperature={temp_min}, and chance of rain={precip_prob}")
              st.session_state.conversation_history.append(f"You: {st.session_state.input_text}")
              st.session_state.conversation_history.append(f"Weather man: {response2.text}")
              st.session_state.input_text = ''

    
     output_container = st.container()
     with output_container:
         for message in st.session_state.conversation_history:
             st.write(message)

     st.write("")
     st.write("")
   
     input_container = st.container()
     st.text_input(" ", key="input_text", on_change=submit, placeholder="Your question...")
    
        
         


            


