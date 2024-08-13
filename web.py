import streamlit as st
from classifier import Model

st.title("GOOSE Attack Detector")

data = st.text_input("enter data")
model = Model()


if st.button("submit") or data:
	try:
		data = data.split(',')
		data = [[float(i) for i in data]]
		st.title(model.predict(data)[0])
	except ValueError:
	st.error("There is a missing value or there is more than the expected number of values.")