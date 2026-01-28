import streamlit as st
st.title("Demo: Simple Streamlit App")
st.write("This is a simple Streamlit application demonstrating basic functionality.")
st.number_input("Enter a number:",key="input1")
st.number_input("Enter a number:",key="input2")
st.button("Submit",key="name_button1"),
if st.button=="name_button1":
    st.write(name_input1+name_input2)


