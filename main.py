import streamlit as st
import os
import base64
import time

st.set_page_config(page_title="Quantora Foundation", page_icon="🏆", layout="wide")

# Background video
video_path = os.path.join("static", "176434-855480487_small.mp4")
if os.path.exists(video_path):
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
        encoded_video = base64.b64encode(video_bytes).decode()
    st.markdown(f"""
    <video autoplay loop muted playsinline style="position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;">
    <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
.hero {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    flex-direction: column;
    animation: fadeIn 2s ease-in-out;
}
.hero h1 {
    font-size: 5em;
    color: #f1c40f;
    animation: glow 2s infinite alternate;
}
.hero h2 {
    font-size: 2em;
    margin-top: 20px;
    color: #f1c40f;
}
.stButton>button {
    background-color: #f39c12;
    color: #2c3e50;
    padding: 15px 40px;
    border-radius: 50px;
    text-transform: uppercase;
    font-size: 18px;
    font-weight: bold;
    border: none;
    cursor: pointer;
    margin-top: 30px;
    transition: all 0.4s ease;
}
.stButton>button:hover {
    background-color: #e67e22;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.6);
    transform: scale(1.1);
}
.footer {
    text-align: center;
    background-color: #2c3e50;
    color: white;
    padding: 30px;
    animation: slideUp 1s ease-in-out;
}
@keyframes glow {
    0% { text-shadow: 0 0 10px #ff00ff; }
    50% { text-shadow: 0 0 20px #ff00ff; }
    100% { text-shadow: 0 0 10px #ff00ff; }
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
@keyframes slideUp {
    from {transform: translateY(100px); opacity: 0;}
    to {transform: translateY(0); opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# Navigation State
if "page" not in st.session_state:
    st.session_state.page = "home"


def go_to_projects():
    with st.spinner("Loading projects..."):
        time.sleep(1.5)
    st.session_state.page = "projects"


def go_to_about():
    with st.spinner("Loading About Us..."):
        time.sleep(1.2)
    st.session_state.page = "about"


# HOME PAGE
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
        <h1>Quantora Foundation</h1>
        <h2>Empowering communities to reach their highest potential</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Join the Movement"):
        go_to_projects()

# PROJECTS PAGE
elif st.session_state.page == "projects":
    st.title("🌟 Our Projects")
    st.markdown("Explore our featured innovations below:")
    st.markdown('<div style="animation:fadeIn 1.5s;">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.header("🌐 Quantora Search Engine")
        st.markdown("""
        - **Privacy-focused & ad-free**
        - **AI-generated result summaries**
        - **No tracking or surveillance**
        """)
        st.markdown("[👉 Visit Quantora Search Engine](https://quantora-search-engine.streamlit.app/)")

        st.header("💡 Quantora AI")
        st.markdown("""
        - **Intelligent chatbot with natural conversation**
        - **Multi-language support**
        - **Creative, helpful, and ethical**
        """)
        st.markdown("[👉 Visit Quantora AI](https://quantoraai.streamlit.app/)")

    with col2:
        st.header("📱 Quantora Social Media")
        st.markdown("""
        - **AI moderation for safety**
        - **Post, like, and comment easily**
        - **Private and abuse-free platform**
        """)
        st.markdown("[👉 Visit Quantora Social Media](https://firebox-social.streamlit.app/)")

        st.header("📰 Quantora News")
        st.markdown("""
        - **AI-powered news summaries**
        - **Fact-checked, unbiased content**
        - **Personalized news feed**
        """)
        st.markdown("[👉 Visit Quantora News](https://quantoranews.streamlit.app/)")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("---")

    if st.button("About Us"):
        go_to_about()

# ABOUT US PAGE
elif st.session_state.page == "about":
    st.title("🚀 About Quantora Foundation")
    st.markdown("""
    ### How It All Began:
    Quantora Foundation was envisioned as a **futuristic movement** to build ethical, AI-powered tools that **empower people, preserve privacy, and unlock human potential**.

    Founded in 2025 by **Kushagra Srivastava**, Quantora started as a dream to merge innovation with integrity.

    ---
    ### 🌟 Our Mission:
    > "We believe the future is not something we enter, it's something we create."  
    > — Leonard Sweet

    Our mission is to **democratize technology**, make it useful for all, and promote **freedom of knowledge and communication**.

    ---
    ### 💬 Best Quotes That Inspire Us:
    - “The best way to predict the future is to create it.” — Peter Drucker  
    - “Technology like art is a soaring exercise of the human imagination.” — Daniel Bell  
    - “In a world full of noise, we build clarity.”

    ---
    ### 👤 Who Created Quantora?
    Quantora was created by **Kushagra Srivastava**, a passionate technologist, innovator, and student with a vision to make technology work for **everyone**, not just a few.

    He also created:
    - Quantora AI
    - Quantora Social Media
    - Quantora News
    - Firebox Search
    
    He also has a channel - Coding Adventure With Kushagra

    ---
    """)

    st.video('https://youtu.be/CwuowZv57Ow?si=9nOunt4Yj2HbyrJN')

    if st.button("🔙 Back to Projects"):
        st.session_state.page = "projects"

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 Quantora Foundation. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
