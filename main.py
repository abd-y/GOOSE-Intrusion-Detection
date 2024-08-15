import streamlit as st
from classifier import Model
import pandas as pd

if "text" not in st.session_state:
	st.session_state.text = ""

def submit():
	data = [[float(stnum.strip()), float(time.strip()), float(sqNum.strip())]]
	st.session_state.text = model.predict(data)[0] + " packet"

st.title("GOOSE Attack Detector")

model = Model()
X = model.X_test
X["class"] = model.y_test

time = st.text_input("timeAllowedtoLive")
stnum = st.text_input("stnum")
sqNum = st.text_input("sqNum")
if  st.button("submit"):
	submit()
output = st.title(st.session_state.text)

st.text("bellow some data that the model never seen before:")

st.text(X.head(-13).to_string(index=False))

