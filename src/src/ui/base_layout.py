import streamlit as st

def style_base_home():
    st.markdown("""
    <style>
    .stApp {
        background: #5865F2 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def style_base_dashboard():
    st.markdown("""
    <style>
    .stApp {
        background: #5865F2 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

    /* Hide Top Bar of streamlit */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .block-container {
        padding-top: 2.5rem !important;
        max-width: 900px !important;
    }

    h1 {
       font-family: 'Climate Crisis', sans-serif !important;
       font-size: 3.5rem !important;
       line-height: 1.1 !important;
       margin-bottom: 0.3rem !important;
       color: white !important;
       text-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    h2 {
       font-family: 'Climate Crisis', sans-serif !important;
       font-size: 3.5rem !important;
       line-height: 1.1 !important;
       margin-bottom: 0.3rem !important;
       color: white !important;
       text-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }

    h3, h4, p {
        font-family: 'Outfit', sans-serif;
        color: rgba(255,255,255,0.9) !important;
    }

    button {
        border-radius: 1.5rem !important;
        background: #EB459E !important;
        color: white !important;
        padding: 10px 28px !important;
        border: none !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25) !important;
        transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
    }

    button:hover {
        transform: translateY(-3px) scale(1.03) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
    }

    button[kind="secondary"] {
       border-radius: 1.5rem !important;
       background: #EB459E !important;
       color: white !important;
       padding: 10px 28px !important;
       border: none !important;
       font-family: 'Outfit', sans-serif !important;
       font-weight: 600 !important;
       box-shadow: 0 4px 14px rgba(0,0,0,0.25) !important;
       transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
    }

    button[kind="tertiary"] {
       border-radius: 1.5rem !important;
       background: #EB459E !important;
       color: white !important;
       padding: 10px 28px !important;
       border: none !important;
       font-family: 'Outfit', sans-serif !important;
       font-weight: 600 !important;
       box-shadow: 0 4px 14px rgba(0,0,0,0.25) !important;
       transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
    }
    </style>
    """, unsafe_allow_html=True) 