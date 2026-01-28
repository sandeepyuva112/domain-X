import streamlit as st

st.title("Simple Streamlit App")
st.write("This is a simple Streamlit application demonstrating basic functionality.")
number1=st.number_input("Enter a number:", min_value=0, max_value=100)
number2=st.number_input("Enter another number:", min_value=0, max_value=100)
st.button("Sum the numbers") 
def on_button_click():
    st.write("The sum is:")
    st.write(number1 +number2)
on_button_click()
st.download_button('downlopd', data='jpg', file_name='wallpaper.png')

import pandas as pdgt
import pandas as pd


st.title("My First Streamlit App")
st.write("Hello Streamlit")

# Section 1: Basic Input
st.subheader("Section 1: Basic Input")
name1 = st.text_input("Enter your name", key="name1")
age1 = st.number_input("Enter your age", min_value=1, key="age1")
if st.button("Submit", key="btn1"):
    st.write("Name:", name1)
    st.write("Age:", age1)

# st.divider()


# Section 3: Session State (Persistent Data)
st.subheader("Section 3: Add Students (Persistent)")
name2 = st.text_input("Enter your name", key="name2")
age2 = st.number_input("Enter your age", min_value=1, key="age2")
if "student_list" not in st.session_state:
    st.session_state.student_list = []
if st.button("Submit", key="btn2"):
    if name2:
        st.session_state.student_list.append({"name": name2, "age": int(age2)})
        st.success("Student added")
    else:
        st.warning("Please enter a name")
st.table(st.session_state.student_list)
st.divider()
# Section 4: Bar Chart
st.subheader("Section 4: Subject Marks")
data = {
    "Subject": ["Maths", "Physics", "Chemistry"],
    "Marks": [85, 90, 95]
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Subject"))
