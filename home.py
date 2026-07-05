import streamlit as st
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#141E30,#243B55);
    color:white;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config( page_icon="💻",page_title="Portfolio",layout="wide")

col1,col2=st.columns(2)

with col1:
    st.image("assets/pic.jpeg",width=300,channels="RGB", output_format="auto")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown(
   "<h3 >💻 Code. Create. Innovate.</h3>",
   unsafe_allow_html=True
   )
    st.write(" ")
    st.write(" ")   
    st.markdown("<h3>🐈‍⬛ github</h3>",unsafe_allow_html=True)
    st.link_button("click here","https://github.com/Saivardhan2527")
    st.write(" ")
    st.write(" ")
    st.markdown("<h3>💻 linkedin</h3>",unsafe_allow_html=True)
    st.link_button("click here","https://www.linkedin.com/in/kolakani-sai-vardhan-16a57031a/")
    
    

with col2:
    st.title("👋Hello EveryOne!!")
    st.subheader("🚀 My name is Sai Vardhan")
    st.write("Recent graduate with a passion for software development, problem-solving, and lifelong learning.")
    st.divider()
    st.markdown("<h3 >📝 Summary</h3>",unsafe_allow_html=True)    
    st.write(" B.Tech (Internet of Things) graduate, CGPA 9.2/10, with hands-on Java development experience "
    "and a strong foundation in Object-Oriented Programming, Data Structures & Algorithms, and Database Management Systems (DBMS). " \
    "Built three end-to-end projects spanning Java-based application logic, machine learning, and IoT systems, " \
    "including a peer-reviewed paper presented at an international engineering conference (ICRTETM 2026)." \
    " Comfortable working across the stack — Java, SQL, REST-style APIs, and React front ends — with practical exposure to Spring Boot "
    "and Maven through Java Full-Stack training. Seeking an entry-level Java Developer role to write clean, maintainable code and " \
    "contribute to production systems from day one. ")
  

    st.divider()

    st.markdown("<h3>📄 Download my resume below:<h3>",unsafe_allow_html=True)
    st.download_button("resume",open("assets/resume.pdf","rb"),file_name="resume.pdf")
    
    st.divider()

    st.markdown("<h3 >🎓 Education</h3>",unsafe_allow_html=True)    
    st.markdown("**🏫 B.Tech in Internet of Things (IoT)**")
    st.write("Malla Reddy University, Hyderabad (2022–2026)")
    st.markdown("**CGPA : 9.2 / 10**")

    st.write("")

    st.markdown("**🏫 Intermediate**")
    st.write("Alphores Junior College, Karimnagar (2020–2022)")
    st.markdown("**CGPA : 9.8 / 10**")

    st.divider()

    st.markdown("<h3>📬 Contact</h3>",unsafe_allow_html=True)
    st.write("📱 6305123250")
    st.write("📧 saivardhankolakani7@gmail.com")

    st.divider()

    st.subheader("click here to take a look on my Projects") 
    if st.button("🚀 View Projects"):
       st.switch_page("pages/project.py")
    
    st.divider()
    st.subheader("click here to take a look on my certications")
    if st.button("my certifications"):
       st.switch_page("pages/certifications.py")

    st.divider()
    st.subheader("click here to take a look on my skills")
    if st.button("my skills"):
       st.switch_page("pages/skills.py")


