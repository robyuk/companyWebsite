import streamlit as st
from sendEmail import sendEmail
import re

# Regular expression for email address syntax
regex = re.compile(r'([A-Za-z0-9]+[.-_-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

userEmail = st.text_input('Enter email address')

with open('topics.csv', 'r') as file:
    topicList = file.readlines()

topic = st.selectbox('Select topic', topicList[1:])
message = st.text_area('Message:')
button = st.button('Send email')

if button:
    if message == '':
        st.info('Please enter a message')
    elif re.fullmatch(regex, userEmail):  #  valid email address syntax?
        message = f"""Subject: Contact Us email from {userEmail}\n
            From: {userEmail}
            Topic: {topic}
            {message}"""

        sendEmail(msg=message)
        st.info('Your email was sent')
    else:
        st.info("Please enter a valid email address")
