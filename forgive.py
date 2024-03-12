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
    poems = [
        "Roses are red, violets are blue, I forgot your birthday, my love so true. For my mistake, I deeply rue, Let me make it up with something special, just for you.",
        "In the realm of dates, I made a blunder, Your birthday slipped my mind, torn asunder. With heartfelt words, I seek to convey, My deepest apologies and a special day.",
        "A calendar slip, a grievous crime, I forgot your birthday, dear partner in crime. Let my words weave an apology so fine, And a plan to make it up, uniquely designed.",
        "Time betrayed me, a lapse so grave, I forgot your birthday, my heart to save. Let these lines serve as my sincere plea, For your forgiveness and a date with glee.",
        "The date slipped away, from memory it flew, I forgot your birthday, my love so true. Let this poetic apology be a start, To heal the wound and mend your heart."
    ]

    return random.choice(poems)

def main():
    st.title('Forgiveness App')

    if st.button('Apologize'):
        apology_message = get_apology()
        st.write(apology_message)

if __name__ == '__main__':
    main()
