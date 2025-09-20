import streamlit as st
from db_config import get_connection

st.set_page_config(page_title="Job Application Form", page_icon="📝")

st.title("Job Application Form")

with st.form("job_form"):
    # Core fields
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
    last_company = st.text_input("Last Working Company")

    # Extra fields
    full_name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    skills = st.text_area("Skills (comma separated)")
    education = st.text_input("Highest Education")
    location = st.text_input("Current Location")
    linkedin = st.text_input("LinkedIn Profile URL")
    github = st.text_input("GitHub Profile URL")
    portfolio = st.text_input("Portfolio/Website URL")
    expected_salary = st.number_input("Expected Salary", min_value=0.0, step=1000.0)
    notice_period = st.text_input("Notice Period (e.g., 30 days)")
    additional_notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit Application")

    if submitted:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO applicants 
                (email, password, experience_years, last_company, full_name, phone, skills, education, location, linkedin, github, portfolio, expected_salary, notice_period, additional_notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (email, password, experience, last_company, full_name, phone, skills, education, location, linkedin, github, portfolio, expected_salary, notice_period, additional_notes))
            conn.commit()
            cursor.close()
            conn.close()
            st.success("✅ Application submitted successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
