import streamlit as st

# Set page config
st.set_page_config(page_title="Sophos", page_icon="🧠", layout="wide")

# Custom CSS for the animated background and styling
st.markdown("""
<style>
body {
    background-color: black;
    color: white;
    margin: 0;
    padding: 0;
    overflow: hidden;
}

.stApp {
    background-color: transparent;
}

.sigmoid-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    overflow: hidden;
}

.sigmoid {
    position: absolute;
    width: 200%;
    height: 100%;
    animation: wave 8s infinite linear;
}

h1, h2, h3, p, a, li {
    color: white !important;
}

.stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: white !important;
}

.download-link {
    display: inline-block;
    padding: 10px 20px;
    margin: 10px;
    background-color: #808080;  /* Grey background */
    color: white !important;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
}

.instructions {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    margin-top: 30px;
}

/* Specifically target Streamlit's subheader */
.stSubheader {
    color: white !important;
}
</style>

<div class="sigmoid-container">
    <svg class="sigmoid" viewBox="0 0 1440 320" preserveAspectRatio="none">
        <path fill="rgba(255,255,255,0.1)" d="M0,160L48,181.3C96,203,192,245,288,261.3C384,277,480,267,576,234.7C672,203,768,149,864,128C960,107,1056,117,1152,138.7C1248,160,1344,192,1392,208L1440,224L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
    </svg>
    <svg class="sigmoid" viewBox="0 0 1440 320" preserveAspectRatio="none" style="animation-delay: -4s;">
        <path fill="rgba(255,255,255,0.05)" d="M0,64L48,80C96,96,192,128,288,128C384,128,480,96,576,90.7C672,85,768,107,864,122.7C960,139,1056,149,1152,144C1248,139,1344,117,1392,106.7L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
    </svg>
</div>
""", unsafe_allow_html=True)

# App content
st.title("Sophos")
st.subheader("Supercharging human knowledge")

st.markdown("""
<a href="https://testflight.apple.com/join/cy4MTPpD" class="download-link">Download Desktop App (Beta)</a>
<a href="https://testflight.apple.com/join/W9DmJfwA" class="download-link">Download Mobile App (Beta)</a>

<div class="instructions">
<h2>Get started:</h2>
<ol>
    <li>Download the Desktop app
    <ul>
        <li>Log in</li>
        <li>Give Sophos permission to screen capture</li>
        <li>Capture information on screen to make cards</li>
    </ul>
    </li>
    <li>Download the Mobile app
    <ul>
        <li>Log in with the same account</li>
        <li>Start studying!</li>
    </ul>
    </li>
</ol>
</div>
""", unsafe_allow_html=True)