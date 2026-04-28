import streamlit as st
from utils.loader import load_and_split_documents
from utils.embedder import create_vector_store
from utils.rag_chain import get_rag_chain

st.title("Financial RAG Chatbot")

uploaded_file = st.file_uploader("Upload Financial PDF", type=["pdf"])

if uploaded_file:
    with open("data/financial_report.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded Successfully")

    if st.button("Process Document"):
        chunks = load_and_split_documents("data/financial_report.pdf")
        create_vector_store(chunks)
        st.success("Vector Store Created Successfully")

query = st.text_input("Ask your financial question:")

if query:
    chain = get_rag_chain()
    response = chain.invoke({"query": query})

    st.subheader("Answer")
    st.write(response["result"])