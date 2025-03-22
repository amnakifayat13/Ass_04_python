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

st.title(":blue[Number Guessing Game-Computer]")

x = 10 
random_number = random.randint(1, x)

# Use session state to store variables across reruns
if "random_number" not in st.session_state:
    st.session_state.random_number = random_number

guess = st.number_input(f"Guess a number between 1 and {x}:", min_value=1, max_value=x, step=1)

if st.button("Submit Guess"):
    if guess < st.session_state.random_number:
        st.warning("Guess again. Too Low")
    elif guess > st.session_state.random_number:
        st.warning("Guess again. Too High")
    else:
        st.balloons()
        st.success(f"Yeeyyyy! Congrats! You have guessed the number {st.session_state.random_number}")
        # Reset the game by generating a new random number
        st.session_state.random_number = random.randint(1, x)
