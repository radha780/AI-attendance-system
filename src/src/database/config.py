import streamlit as st
from supabase import create_client, Client

superbase: Client = create_client(
    st.secrets["SUPERBASE_URL"],
    st.secrets["SUPERBASE_KEY"]
)