#%%writefile app.py
from itertools import chain
import streamlit as st
import pickle 
import pandas as pd

pickle_in = open("classifier.pkl","rb")
classifier =pickle.load(pickle_in)


def prediction(input_set):
    prediction = classifier.predict([input_set])
    return prediction



def main():
  st.title("Testing Boston House")
  html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """

  st.markdown(html_temp,unsafe_allow_html=True)

  crim = st.text_input("CRIM","Type Here")
  zn = st.text_input("ZN","Type Here")
  indus = st.text_input("INDUS","Type Here")
  chas = st.text_input("CHAS","Type Here")
  nox = st.text_input("NOX","Type Here")
  rm = st.text_input("RM","Type Here")
  age = st.text_input("AGE","Type Here")
  dis = st.text_input("DIS","Type Here")
  rad = st.text_input("RAD","Type Here")
  tax = st.text_input("TAX","Type Here")
  ptratio = st.text_input("PTRATIO","Type Here")
  b = st.text_input("B","Type Here")
  lstat = st.text_input("LSTAT","Type Here")



  result=""
  if st.button("Predict"):
      input_set = [crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]
      result = prediction(input_set)
      st.success('The output is {}'.format(result))
  if st.button("About"):
      st.text("Lets LEarn")
      st.text("Built with Streamlit")

#if __name__=='__main__':


main()
