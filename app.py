import streamlit as st

from calc import add

st.title("js-lab")
st.write("Add two numbers.")

a = st.number_input("First number", value=1.0)
b = st.number_input("Second number", value=2.0)

st.write("Sum:", add(a, b))
