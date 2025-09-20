import os
import mysql.connector
from dotenv import load_dotenv

# Load local .env file (only works locally)
load_dotenv()

def get_connection():
    """
    Returns a MySQL connection using environment variables.
    Works locally (via .env) or on Streamlit Cloud (via secrets).
    """
    # Try Streamlit secrets first
    try:
        import streamlit as st
        return mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"],
            database=st.secrets["mysql"]["database"]
        )
    except ImportError:
        # Local fallback using .env
        return mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
        )
