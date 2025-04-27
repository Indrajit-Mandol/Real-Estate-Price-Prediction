import os
import pickle
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components

# importing the smaller apps
from ml_app import run_ml_app
from eda_app import run_eda_app

# --- Main page header HTML ---
html_temp = """
    <div style="background-color:#4CAF50;padding:20px;border-radius:12px;margin-bottom:20px">
        <h1 style="color:white;text-align:center;">🏡 Real Estate Price Prediction App</h1>
        <h4 style="color:white;text-align:center;">By Indrajit Mandol 🚀</h4>
    </div>
    """

def main():
    components.html(html_temp)

    # --- Sidebar Menu ---
    st.sidebar.title("Navigation Menu 📑")
    menu = ["🏠 Home", "📊 Data Analysis", "🔮 Prediction", "ℹ️ About"]
    choice = st.sidebar.radio("Go to", menu)

    # --- Pages ---
    if choice == "🏠 Home":
        st.subheader("Welcome to the Real Estate Insights App 🏠")
        img1 = Image.open(os.path.join("IMG", "Realty_Growth.jpg"))
        st.image(img1, use_column_width=True)

        st.markdown("""
            ### 🧠 Thinking Ahead
            Real estate prices are deeply cyclical and are affected by many external factors.

            Whether you are buying a new property or using your home's equity, it's important to analyze both broader market conditions and your specific property to forecast future values.
            
            ---
            ### 🔥 What this App Offers:
            - Predicts property prices based on input features
            - Helps you estimate your budget smartly
            - Visualizes important real estate trends
        """)
        st.success("👉 Use the sidebar to start exploring!")

    elif choice == "📊 Data Analysis":
        st.subheader("Explore the Data 📈")
        run_eda_app()

    elif choice == "🔮 Prediction":
        st.subheader("Predict Property Prices 🏡")
        run_ml_app()

    else:
        st.subheader("About this Project ℹ️")

        path_to_html = os.path.join("IMG", "mumbai_property.html")
        with open(path_to_html, 'r', encoding='utf-8') as f:
            html_data = f.read()

        components.html(html_data, height=400, scrolling=True)

        st.markdown("---")
        st.subheader("🔗 Connect with Me")

        with st.expander("Social Links 📬"):
            socials = {
                "LinkedIn 🔗": "https://www.linkedin.com/in/indrajit-mandol",
                "GitHub 🐙": "https://github.com/Indrajit-Mandol",
                "Email 📧": "mailto:indrajit142024@gmail.com"
            }
            platform = st.selectbox("Choose a platform", list(socials.keys()))
            link = socials[platform]
            st.markdown(f"[Click Here to Open]({link})", unsafe_allow_html=True)

        st.info("Thanks for visiting! 🙏 Hope you find it useful.")

if __name__ == "__main__":
    main()
