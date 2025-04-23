import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Hamza Syed's Portfolio",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Main Page Title
st.title("🌐 Welcome to Hamza Syed's Python World")
st.caption("Turning ideas into code, one project at a time.")

# About Section
st.header("👨‍💻 About Me")
st.write("""
Hi! I'm *Hamza Syed*, a passionate Python & Frontend Developer 🚀  
Currently building awesome apps using *Python* and *Streamlit* for fun and learning.  
I love creating interactive tools, solving problems, and exploring the power of code.
""")

# Projects Section
st.header("🛠 My Python Projects")
st.markdown("""
Here are some of my featured projects:
- 🔐 [*Password Generator*](https://passwordgeneratorpythonproject-wyowzurdsh8u2tuy2fxl3c.streamlit.app/) – A secure password creator built with Streamlit  
- ⚖️ [*BMI Calculator*](https://bmicalculatorpythonproject-bgx8esdzzwvgdkxyvgqorb.streamlit.app/) – A BMI checker with health tips  
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤ by [Hamza Syed](https://github.com/hamzaaleem230)")

# Sidebar Navigation & Social Links
st.sidebar.title("📂 Navigation")
st.sidebar.markdown("✔️ [Home](#welcome-to-hamza-syeds-python-world)")
st.sidebar.markdown("📁 [Projects](#my-python-projects)")
st.sidebar.markdown("👨‍💻 [About Me](#about-me)")

st.sidebar.title("📬 Connect With Me")
st.sidebar.markdown("🔗 [GitHub](https://github.com/hamzaaleem230)")
st.sidebar.markdown("✉️ [Email Me](mailto:hamzaaleem230@gmail.com)")