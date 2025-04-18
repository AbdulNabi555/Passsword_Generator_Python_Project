import streamlit as st
import string
import random
def generate_password(length, use_digit, use_special):
    charachters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(charachters) for _ in range(length))
st.title("Password Generator")
length = st.slider("Select Password Length", min_value= 6, max_value=32, value=16)
use_digit = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")
if st.button("Generate Password"):
    password = generate_password(length, use_digit, use_special)
  
    st.success(f"Generated Password: {password}")
st.write("Build 💻 by [Abdul Nabi](https://github.com/AbdulNabi555)")