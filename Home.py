# This is a Python script using streamlit to make a company website.

# To run the website, type the following in the Terminal window (without the quotes):
"""streamlit run Home.py"""

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import streamlit as st
import pandas

imageDir = 'images/'
companyName = 'The Best Company'
description = """
This is the website for our company.  Founded in 2016, beginning a tradition of unparalleled customer 
service and quality IT consultancy. We’re dedicated to your happiness. That means we 
arrive on time and investigate your system before diving blindly into the situation. We get it right 
the first time. Regardless of the size of the job or its complexity, your satisfaction is most 
important to us. And as a thoroughly family-owned company, you can trust us to give your family the 
same attention we give to ours. If your IT system, hardware, software, cloud, security, or storage
isn’t working correctly, give us a call immediately. We’ll schedule an appointment."""
staff = pandas.read_csv('staff.csv')

st.set_page_config(page_title=companyName, layout='wide')

st.title(companyName)
st.info(description)
st.header('Our Team')

col1, mtCol1, col2, mtCol2, col3 = st.columns([2, 1, 2, 1, 2])

for col, start, end in [(col1, 0, 4), (col2, 4, 8), (col3, 8, 12)]:
    with col:
        for index, row in staff[start:end].iterrows():
            st.subheader(f"{row['first name']} {row['last name']}".title())
            st.write(row.role)
            st.image(imageDir + row.image)
            st.title(' ')
