import streamlit as st
import random

# Custom Styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, rgb(223, 129, 187), rgba(135, 206, 235, 1));
            color: white;
        }
        .stTextInput>div>div>input {
            border: 2px solid rgb(170, 49, 130);
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: rgb(90, 5, 62);
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: rgb(63, 5, 37);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color: white;'>💻 Computer Guessing Game by User</h1>", unsafe_allow_html=True)
st.write("Think of a number between 1 - 50, and the computer will try to guess it.")

if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 50
if "guess" not in st.session_state:
    st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)

st.subheader(f"Is your number: {st.session_state.guess}?")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Too Low"): 
        st.session_state.low = st.session_state.guess + 1
        if st.session_state.low <= st.session_state.high:
            st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            st.rerun()

with col2: 
    if st.button("Too High"):
        st.session_state.high = st.session_state.guess - 1
        if st.session_state.low <= st.session_state.high:
            st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            st.rerun()

with col3:
    if st.button("Correct!"):
        st.balloons()
        st.success(f"You have guessed the correct number! {st.session_state.guess}")
    
