import re
import streamlit as st

# page styling
st.set_page_config(
    page_title="Password Strength Meter By Mujahid Shaikh!",
    page_icon=":lock:",
    page_icon=":pencil:",
    layout="wide",
    initial_sidebar_state="expanded",
)
# custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: #4CAF50; font-size: 18px; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;}
    .stButton button:hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

# title and description
st.markdown("<h1>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
st.write("Enter your password below to check its ssecurity level. 🔍")

# function to check password strenth
def check_password_strenth(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long.**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters.**")

    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one digit (0-9).**")

    # special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*(),.?\":{}|<>)**")

# display password strength results
    if score == 4:
        st.success("✅ Password is **strong!** your password is secure.")
    elif score == 3:
        st.warning("⚠️ Password is **moderate.** Consider adding more complexity.")
    else:
        st.error("❌ Password is **weak.** Please improve your password.")

    # display feedback
    if feedback:
        with st.expander("📝 **Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong and secure. 🔒")

# button to check password strength
if st.button("Check Password Strength"):
    if password:
        check_password_strenth(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")