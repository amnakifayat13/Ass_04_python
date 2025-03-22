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


st.title(":rainbow[📄Paper, ⛰️Rock & ✂️Scissor Game]")
user_action = st.selectbox("Enter a choice:", ["Rock", "Paper", "Scissor"])
possible_actions = ["Rock", "Paper", "Scissor"]
computer_action = random.choice(possible_actions)
st.write(f"You chose {user_action}, computer chose {computer_action}.")

if user_action == computer_action:
    st.write(f"Both players selected {user_action}. It's a tie!")
elif user_action == "Rock":
    if computer_action == "Scissor":
        st.balloons()
        st.success("Rock smashes Scissor! You win!")
    else:
        st.write("Paper covers Rock! You lose.")
elif user_action == "Paper":
    if computer_action == "Rock":
        st.balloons()
        st.success("Paper covers Rock! You win!")
    else:
        st.write("Scissor cuts Paper! You lose.")
elif user_action == "Scissor":
    if computer_action == "Paper":
        st.balloons()
        st.success("Scissor cuts Paper! You win!")
    else:
        st.write("Rock smashes Scissor! You lose.")