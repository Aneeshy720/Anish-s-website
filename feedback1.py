import streamlit as st
import pandas as pd 
import os
folder_path = 'data/feedbacks.csv'
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists(folder_path):
    df = pd.DataFrame(columns=['Name','Feedback','Rating'])
    df.to_csv(folder_path,index=False)

name = st.text_input("Enter your name :-",key='nam')
feed = st.text_input("Enter your feedback :-",key = 'fed')
rating = st.slider("Rate us from 1 - 5",min_value=1,max_value=5,step=1,value=1)

col1,col2 = st.columns([0.1,0.9])
with col1:
    submit = st.button('Submit')
with col2:
    clear = st.button('Clear')

emoji_holder = st.empty()

if rating ==1:
    emoji_holder.subheader("We will surely try to improve" + ":weary:")
if rating ==2:
    emoji_holder.subheader("We will try to improve your experience"+":slightly_smiling_face:")
if rating ==3:
    emoji_holder.subheader("Thanks"+":smiley:")
if rating ==4:
    emoji_holder.subheader("Thank you so much for your feedback"+":blush:")
if rating ==5: 
    emoji_holder.subheader("Thank you so much, we love your feedback!" + ":partying_face:")