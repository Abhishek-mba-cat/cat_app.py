
import streamlit as st
import json
import os
import random

st.title("🧠 MCQ Practice - QA / VARC / DILR")

# Subject and Level Selection
subject = st.selectbox("Choose Subject", ["QA", "VARC", "DILR"])
level = st.selectbox("Choose Difficulty Level", list(range(1, 11)))

# Build file path
file_path = f"data/{subject}_mcqs_level{level}.json"

# Check if file exists
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        questions = json.load(f)

    if questions:
        # Shuffle questions
        random.shuffle(questions)
        score = 0
        total = len(questions)

        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1}. {q['question']}**")
            options = q['options']
            user_ans = st.radio("Select your answer:", options, key=idx)
            if 'submit' not in st.session_state:
                st.session_state.submit = False

            if st.button(f"Submit Q{idx+1}", key=f"submit_{idx}"):
                if user_ans == q['answer']:
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Incorrect! Correct Answer: {q['answer']}")
                st.session_state.submit = True
                st.markdown("---")

        if st.session_state.submit:
            st.info(f"Your score: {score} / {total}")
    else:
        st.warning("No questions found at this level.")
else:
    st.warning("No MCQ file found for this selection.")
