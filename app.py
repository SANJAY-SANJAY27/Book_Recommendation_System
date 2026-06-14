import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Recommendation System")

try:
    # Load Dataset
    books = pd.read_csv(
        "Books_small.csv",
        low_memory=False,
        encoding="latin-1"
    )

    st.success("Dataset Loaded Successfully ✅")

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows:", books.shape[0])

    with col2:
        st.write("Columns:", books.shape[1])

    st.subheader("Column Names")

    st.write(books.columns.tolist())

    st.subheader("First 5 Rows")

    st.dataframe(books.head())

except Exception as e:
    st.error(f"Error loading dataset: {e}")
