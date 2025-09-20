import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",       # keep as localhost for now
        user="root",            # your MySQL username
        password="K.madan@10121963",  # <-- replace with your actual MySQL password
        database="job_portal"
    )
