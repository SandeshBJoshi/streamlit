import streamlit as st
st.title("Checking the person eligible for vvote or not")
age = st.number_input("Enter your age:")
if st.button("Submit"):
  if age >= 18:
    st.success("you are eligible to vote...")
  else:
    st.write("not eligible to vote...")

