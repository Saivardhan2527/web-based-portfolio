import streamlit as st
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#000000,#434343);
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h3 >📁 Certifications</h3>",unsafe_allow_html=True)   


st.divider()

st.write("•	Java Programming — GeeksforGeeks")
st.write("•	Java Full Stack Development — Udemy")
st.write("•	Cloud Computing Architecture — Great Learning")
st.write("•	SQL — Udemy")
st.write("•	Generative AI — Udacity")


if st.button("return to home"):
    st.switch_page("home.py")