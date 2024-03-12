import streamlit as st
import random

def get_apology():
    apologies = [
        "I'm sorry for forgetting your birthday. You mean the world to me, and I feel terrible about this mistake.",
        "I messed up big time by forgetting your birthday. I promise to make it up to you and show you how much you mean to me.",
        "I can't believe I forgot your birthday. I'm sincerely sorry, and I want to make it right. Let's celebrate together soon.",
        "I owe you a huge apology for forgetting your special day. You deserve all the happiness, and I want to be the one to give it to you.",
        "I feel awful for forgetting your birthday. Please forgive me, and let me make it up to you in the most special way possible."
    ]

    return random.choice(apologies)

def main():
    st.title('Forgiveness App')

    if st.button('Apologize'):
        apology_message = get_apology()
        st.write(apology_message)

if __name__ == '__main__':
    main()
