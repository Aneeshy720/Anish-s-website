import streamlit as st
import pandas as pd
import os
t1,t2,t3,t4 = st.tabs(["Greetings","About Me", "Free time activities","Sports Cars"])
with t1:
    st.header("Hello!")
    st.subheader("This is a simple website about me and what I like to do to pass time 😃.")
    st.image("Lambo.jpeg",width = 400)
    st.image("bugatti.jpeg", width = 500)
with t2: 
    st.header("Anish Vobilisetti")
    st.subheader("Hi, my name  is Anish and I live in Pleasanton California. I go to Thomas Hart Middle School.")
    st.subheader("My phone number is 925-344-3261")
with t3:
    st.header("Free time activities")
    st.subheader("In my free time, I like to go to the park and play basketball or soccer with my friends. When I'm at home, I like to play Fortnite on my xbox. Also, I like to spend time with my family.")
with t4:
    st.header("The fastest cars in the world")
    date = st.date_input("Date :date:") #:date: is to display the emoji for a calendar, you can use this syntax for other emoji names ex: :sunglasses:
    category = st.selectbox('Category:sunglasses:',("Lamborghini","Bugatti","Ferrari","Corvette"))
    if category=="Lamborghini":
        st.write("Lamborghini is an Italian luxury sports car and SUV manufacturer based in Sant'Agata Bolognese.")
        st.image("lamboengine.jpeg")
    elif category=="Bugatti":
        st.write("The top speed is 420 km/h (261 mph). Bugatti is the only automaker to build a W16 engine that produces over 1,500 hp.")
        st.image("bugattiengine.jpeg")
    elif category=="Ferrari":
        st.write("Italian luxury sports car manufacturer based in Maranello, Italy. Founded in 1939 by Enzo Ferrari (1898 - 1988), the company built its first car in 1940, adopted its current name in 1945, and began to produce its current line of road cars in 1947.")
        st.image("ferrariengine.jpeg")
    elif category=="Corvette":
        st.write("The 2024 Chevrolet Corvette is a mid-engine performance car with a starting price of $68,300. It has a 6.2-liter V-8 engine that produces 490 horsepower and 470 pound-feet of torque, and can accelerate from 0 to 60 mph in 2.9 seconds.")
    info = st.text_input("Info:infinity:")
    st.subheader("So after looking at all this information on these awesome cars, which one would you like to own if you had to choose one?")
    final = st.selectbox("Final Choice",("Lamborghini","Bugatti","Ferrari","Corvette"))
    def clear():
        st.session_state.t = " "
        st.write("Hello")
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists("data/carinfo.csv"):
            c_info = pd.DataFrame(columns = ["Date","Category","Info"])
            c_info.to_csv("data/carinfo.csv",index = False)

        df = pd.read_csv("data/carinfo.csv")
        length = len(df) 
        df.loc[length] = [date,info,category]
        df.to_csv("data/carinfo.csv",index=False)
        st.balloons()
    submit = st.button("SUBMIT:white_check_mark:",on_click = clear )
    


