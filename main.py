import random
import streamlit as st

def generate_number():
    if "target" not in st.session_state:
        st.session_state.target = random.randint(1, 10)

def check_guess(guess):
    if guess < st.session_state.target:
        return "Too low! Try again."
    elif guess > st.session_state.target:
        return "Too high! Try again."
    else:
        return " Correct 🎉 You guessed the right number."
def reset_game():
    st.session_state.target = random.randint(1, 100)
    st.session_state.message = "Game reset! Start guessing again."

st.title("Number Guessing Game 🎮")
generate_number()

st.write("Guess a number between 1 and 10.")

guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1, format="%d")

if st.button("Submit Guess"):
    message = check_guess(guess)
    st.session_state.message = message

if "message" in st.session_state:
    st.write(st.session_state.message)

if st.button("Restart Game"):
    reset_game()


st.write("-----")
st.write("Made with ❤️ by [Mudasir Sohail](https://www.linkedin.com/in/mudasir-sohail-98b399257/) ")