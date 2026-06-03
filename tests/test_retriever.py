from src.retriever import Retriever

def test_query_embedding():
    retriever = Retriever()

    embedding = retriever.get_query_embedding(
        "What is AI?"
    )

    assert embedding is not None
