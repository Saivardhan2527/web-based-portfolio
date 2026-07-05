import streamlit as st

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0F172A,#1E3A8A,#2563EB);
    color:white;
}

</style>
""", unsafe_allow_html=True)
st.markdown("<h3 >👾 Projects</h3>",unsafe_allow_html=True)   


st.subheader("Intelligent Motion-Compensated Stretcher — Real-Time Pitch-Roll Control")
st.divider()
st.write("Java | Embedded Systems | IMU Sensors | Microcontrollers | Real-Time Control | IoT")
st.write("• Designed and implemented a closed-loop pitch-roll stabilization algorithm using IMU sensor feedback and actuator control, reducing stretcher tilt deviation on uneven terrain.")
st.write("• Optimized the real-time control loop and sensor-fusion logic, cutting response latency and improving patient stability during transport.")
st.write("• Co-authored and presented original research at the 6th International Conference on Recent Trends in Engineering, Technology and Management (ICRTETM 2026).")

st.write("")

st.subheader("Safeguarding E-Commerce: Fake Review Detection System")
st.divider()
st.write("Python | NLP | TF-IDF | Logistic Regression | Random Forest | Scikit-learn")
st.write("• Built an NLP and machine learning pipeline using TF-IDF vectorization and Logistic Regression/Random Forest models to classify reviews as genuine or fake.")
st.write("• Implemented text preprocessing and feature extraction to convert unstructured review text into model-ready data, improving classification accuracy.")
st.write("• Developed a web-based interface for real-time review authenticity checks, enhancing consumer trust and platform reliability.")

if st.button("return to home"):
    st.switch_page("home.py")