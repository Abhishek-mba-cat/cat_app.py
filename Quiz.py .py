import streamlit as st
import json
import os
import random

st.set_page_config(page_title="CAT MCQ Practice")

st.title("🎯 CAT MCQ Practice")

# Dropdowns
subject = st.selectbox("Select Subject", ["Quantitative Ability (QA)", "Verbal Ability and Reading Comprehension (VARC)", "Data Interpretation and Logical Reasoning (DILR)"])
level = st.selectbox("Select Difficulty Level", ["Level 1", "Level 2"])

subject_keys = {
    "Quantitative Ability (QA)": "QA",
    "Verbal Ability and Reading Comprehension (VARC)": "VARC",
    "Data Interpretation and Logical Reasoning (DILR)": "DILR"
}

file_path = f"data/{subject_keys[subject]}_mcqs_{level.lower().replace(' ', '')}.json"

# Load questions
if not os.path.exists(file_path):
    st.warning("❗ Questions for this level/subject are not added yet.")
else:
    with open(file_path, "r") as f:
        questions = json.load(f)

    # Shuffle and limit to 15 questions
    random.shuffle(questions)
    questions = questions[:15]

    st.subheader(f"📝 Answer these {len(questions)} questions:")

    # Store answers using session state
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['question']}**")
        st.session_state.answers[i] = st.radio(
            label="Choose one:",
            options=q['options'],
            key=f"q{i}"
        )
        st.markdown("---")

    if st.button("✅ Submit All"):
        score = 0
        st.subheader("📊 Results:")
        for i, q in enumerate(questions):
            user_ans = st.session_state.answers.get(i, "").strip().lower()
            correct_ans = q['answer'].strip().lower()

            if user_ans == correct_ans:
                st.success(f"Q{i+1}: Correct ✅")
                score += 1
            else:
                st.error(f"Q{i+1}: Wrong ❌ (Correct: {q['answer']})")

        st.info(f"🏁 Your Total Score: {score} / {len(questions)}")
