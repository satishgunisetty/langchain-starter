import streamlit as st
from app import process
from dotenv import load_dotenv

load_dotenv()

st.title("AI Agent Demo With LangChain")

st.divider()

with st.form(key="name_form", clear_on_submit=True):
    name = st.text_input("Enter a Name:")
    pressed = st.form_submit_button(label="Press Me!")

    if pressed and name.strip() != '':
        print(f"Pressed: {pressed}, name: {name}")
        st.balloons()
        summary, profile_pic_url = process(name)

        st.divider()
        st.image(image=profile_pic_url, width=300)
        st.divider()

        st.subheader("A Short Summary:")
        st.success(summary.summary)
        st.subheader("Interesting Facts:")
        for fact in summary.facts:
            st.markdown(f"""
            - *{fact}*
            """)

        st.warning("Please fill in the Name.")

