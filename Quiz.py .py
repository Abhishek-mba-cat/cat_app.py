import streamlit as st
import json
import os
import random

st.title("🎯 CAT MCQ Practice")

# Subject and level selection
subject = st.selectbox("Select Subject", ["Quantitative Ability (QA)", "Verbal Ability and Reading Comprehension (VARC)", "Data Interpretation and Logical Reasoning (DILR)"])
level = st.selectbox("Select Difficulty Level", ["Level 1", "Level 2"])

# Convert subject to filename-safe key
subject_keys = {
    "Quantitative Ability (QA)": "QA",
    "Verbal Ability and Reading Comprehension (VARC)": "VARC",
    "Data Interpretation and Logical Reasoning (DILR)": "DILR"
}

file_path = f"data/{subject_keys[subject]}_mcqs_{level.lower().replace(' ', '')}.json"

if not os.path.exists(file_path):
    st.warning("Questions for this level/subject are not yet added.")
else:
    with open(file_path, "r") as f:
        questions = json.load(f)

    random.shuffle(questions)  # Shuffle questions each time

    score = 0
    total = len(questions)

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['question']}**")
        user_answer = st.radio("Choose an option:", q["options"], key=i)

        if st.button(f"Submit Answer {i+1}", key=f"btn{i}"):
            # Debug print (you can remove this after testing)
            st.write(f"User selected: {user_answer}, Correct: {q['answer']}")
            
            if user_answer.strip().lower() == q["answer"].strip().lower():
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong. Correct answer: {q['answer']}")

            st.markdown("---")
