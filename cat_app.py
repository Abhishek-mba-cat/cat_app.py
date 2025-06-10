import streamlit as st
import datetime

st.set_page_config(page_title="CAT Prep Tracker", layout="centered")

st.title("📚 CAT Prep Tracker (Mobile-Friendly)")

date = st.date_input("Date", value=datetime.date.today())
shift = st.selectbox("Shift", ["Day", "Night", "Off"])
varc = st.checkbox("Did VARC?")
quant = st.checkbox("Did Quant?")
lrdi = st.checkbox("Did LRDI?")

if st.button("Save Entry"):
    st.success(f"Saved for {date.strftime('%d %b')} — Shift: {shift}")
    st.write("✅ VARC:", varc)
    st.write("✅ Quant:", quant)
    st.write("✅ LRDI:", lrdi)
else:
    st.info("Fill today's log and tap Save.")
