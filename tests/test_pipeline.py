from src.rag_pipeline import RAGPipeline

def test_pipeline():

    pipeline = RAGPipeline()

    assert pipeline is not None
