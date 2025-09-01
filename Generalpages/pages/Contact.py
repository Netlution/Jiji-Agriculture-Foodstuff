import streamlit as st
import pandas as pd
import mysql.connector

# Title
st.title("Message Us")


# use full screen width
st.set_page_config(layout="wide")  

# Load data
with st.expander("See Table below"):
    # df = pd.read_csv(r"C:\Users\user\Desktop\Web scrapping project\jijipage5_data.csv")
    df = pd.read_csv("data/jijipage5_data.csv")
    
    # Reset index and start from 1
    df_reset = df.head(10).reset_index(drop=True)
    df_reset.index = df_reset.index + 1
    
    st.table(df_reset)

# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # or your server
        user="Netlution",
        password="Samkuljax1995",
        database="contact_form_db"
    )

# Save data to MySQL
def save_to_db(first_name, last_name, address, phone_number, message):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO submissions (first_name, last_name, address, phone_number, message)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, address, phone_number, message))
    conn.commit()
    cursor.close()
    conn.close()



# Simple Form
with st.form("contact_form"):
    st.subheader("Contact Form")
    
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    address = st.text_area("Address")
    phone_number = st.text_input("Phone Number")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Submit")
    
    if submitted:
        missing_fields = []
        if not first_name:
            missing_fields.append("First Name")
        if not last_name:
            missing_fields.append("Last Name")
        if not address:
            missing_fields.append("Address")
        if not phone_number:
            missing_fields.append("Phone Number")
        if not message:
            missing_fields.append("Message")
        
        if missing_fields:
            st.error(f"⚠️ Please fill out the following fields: {', '.join(missing_fields)}")
        else:
            save_to_db(first_name, last_name, address, phone_number, message)
            st.success("✅ Form submitted successfully and saved to database!")
