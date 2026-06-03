import streamlit as st
from src.rag_pipeline import RAGPipeline

st.title('Academic RAG System')
pipeline = RAGPipeline()

uploaded_file = st.file_uploader('Upload PDF', type=['pdf'])

if uploaded_file and st.button('Process Document'):
    with open(uploaded_file.name,'wb') as f:
        f.write(uploaded_file.read())
    pipeline.ingest_document(uploaded_file.name)
    st.success('Document Indexed')

query = st.text_input('Ask a Question')

if st.button('Search'):
    results = pipeline.answer_query(query)
    for r in results:
        st.write(r)
if st.button("Get Answer"):

    result = pipeline.answer_query(
        query
    )

    st.subheader("Answer")

    st.write(
        result["answer"]
    )

    st.subheader("Sources")

    for idx, source in enumerate(
        result["sources"]
    ):

        st.markdown(
            f"### Source {idx+1}"
        )

        st.write(source)
