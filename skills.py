import streamlit as st

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0F2027,#203A43,#2C5364);
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h3 >🧠 Technical Skills</h3>",unsafe_allow_html=True)   

st.divider()
st.write("• Languages: Java, Python, SQL, JavaScript")
st.write("• Core Java: OOP, Collections Framework, Exception Handling, Multithreading, JDBC, Data Structures & Algorithms")
st.write("• Frameworks & Web: Spring Boot, REST APIs, Maven, React.js, HTML, CSS")
st.write("• Databases: MySQL, PostgreSQL, MongoDB")
st.write("• Tools & Platforms: Git, GitHub, IntelliJ IDEA, Eclipse, VS Code, Power BI")
st.write("• Core CS: Operating Systems, Computer Networks, System Design Fundamentals")

if st.button("return to home"):
    st.switch_page("home.py")