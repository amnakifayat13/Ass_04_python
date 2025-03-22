import streamlit as st
from datetime import datetime

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

st.title("👶➡️🧓:rainbow[Age Calculator]")

# Get user input
dob = st.text_input("Enter your date of birth (DD-MM-YYYY): ")

def calculate_age(dob):
    try:
        birth_date = datetime.strptime(dob, "%d-%m-%Y") 
        st.write(birth_date)
        today = datetime.today()
        st.write(today)

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):  
            age -= 1

        return age
    except ValueError:
        return None  
# Display result
if dob:
    age = calculate_age(dob)
    if age is not None:
        st.write(f"Your age is: **{age}** years")
    else:
        st.error("Invalid date format. Please enter in DD-MM-YYYY format.")
