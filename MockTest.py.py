
import streamlit as st
import json
import os
import random

st.title("🧪 Full Mock Test")

# Load all subjects for a combined mock
subjects = ["QA", "VARC", "DILR"]
level = st.selectbox("Choose Difficulty Level", list(range(1, 11)))

# Load questions from all 3 subjects
all_questions = []
for subject in subjects:
    file_path = f"data/{subject}_mcqs_level{level}.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                qs = json.load(f)
                for q in qs:
                    q["subject"] = subject
                all_questions.extend(qs)
            except:
                st.warning(f"Couldn't load questions for {subject}.")

# Shuffle and limit to 15 questions max
random.shuffle(all_questions)
mock_questions = all_questions[:15]

if mock_questions:
    score = 0
    submitted = False

    for idx, q in enumerate(mock_questions):
        st.markdown(f"**Q{idx+1} ({q['subject']})**: {q['question']}")
        user_ans = st.radio("Choose your answer:", q["options"], key=idx)

        if "responses" not in st.session_state:
            st.session_state.responses = {}

        st.session_state.responses[idx] = {
            "user_ans": user_ans,
            "correct_ans": q["answer"],
            "subject": q["subject"]
        }

    if st.button("Submit Mock Test"):
        score = 0
        st.markdown("### ✅ Results")
        for idx, ans in st.session_state.responses.items():
            correct = ans["user_ans"] == ans["correct_ans"]
            if correct:
                score += 1
                st.success(f"Q{idx+1}: Correct ✅ ({ans['subject']})")
            else:
                st.error(f"Q{idx+1}: Incorrect ❌ - Correct: {ans['correct_ans']} ({ans['subject']})")

        st.info(f"Total Score: {score} / {len(mock_questions)}")
else:
    st.warning("No questions available for this level across subjects.")
