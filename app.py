import streamlit as st
import pandas as pd
import pickle as pk
# title 
st.title('Salary classification')

#load pickle file
# model = pk.load('model.pickle')

with open('model.pickle','rb') as file:
# call the load file to 
    model =  pk.load(file)
# forms
age = st.number_input("Enter age :",20,65)
exp = st.number_input("Enter year of experience :",0,30)
education = st.selectbox("Education :",["Bachelor's","Master's","PhD"])
if st.button("Submit"):
    # st.write("Form Submitted")
    if education == "Bachelor's":
        b = 1; m =0 ; p=0
    elif education == "Master's":
        b = 0; m = 1; p = 0
    elif education == "PhD":
        b = 0; m = 0; p =1
    df = pd.DataFrame({
        'Age': [age],
        'Years of Experience': [exp],
        "Bachelor's" : [b],
        "Master's": [m],
        "PhD" : [p]
    })
    df
    
    result = model.predict(df)
    st.write('Output :',result)
