import os
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import mysql.connector


st.set_page_config(page_title="MySQL Data Cleaner", layout="wide")
st.title("MySQL Data Cleaning Web App (Improved Detection)")


# --- CONNECT TO MYSQL ---
try:
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ.get("MYSQL_DATABASE", "data_cleaning_system")
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer_data;")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    st.success("Connected to MySQL and loaded data!")
except Exception as e:
    st.error("❌ Could not connect to MySQL")
    st.write(e)
    st.stop()


# ensure columns exist and correct dtypes
if "age" in df.columns:
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
if "salary" in df.columns:
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")


# --- SHOW ORIGINAL DATA ---
st.subheader("Original Data")
st.dataframe(df)


# --- MISSING VALUES ---
st.subheader("Missing Values")
st.write(df.isnull().sum())


# --- DUPLICATE DETECTION ---
st.subheader("Duplicate Detection")
# By default exclude id from duplicate detection if present
possible_cols = [c for c in df.columns if c != "id"]
st.write("Choose columns to consider when finding duplicates (default: name, email, age, salary)")
default_cols = [c for c in ["name", "email", "age", "salary"] if c in df.columns]
dup_cols = st.multiselect("Duplicate columns", options=possible_cols, default=default_cols)


if len(dup_cols) == 0:
    st.warning("Select at least one column to detect duplicates.")
else:
    dup_mask = df.duplicated(subset=dup_cols, keep=False)
    duplicates = df[dup_mask].sort_values(by=dup_cols)
    st.write(f"Total duplicate rows (based on {dup_cols}): {len(duplicates)}")
    if not duplicates.empty:
        st.dataframe(duplicates)
    else:
        st.write("No duplicates found using the selected columns.")

