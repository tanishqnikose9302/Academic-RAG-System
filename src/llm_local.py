import requests


class LocalLLM:

    def __init__(
        self,
        model_name="gemma3:4b",
        base_url="http://localhost:11434/api/generate"
    ):

        self.model_name = model_name
        self.base_url = base_url

    def generate_answer(
        self,
        query,
        context
    ):

        prompt = f"""
You are an academic assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context,
respond with:
"I could not find the answer in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        try:

            response = requests.post(
                self.base_url,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            result = response.json()

            return result.get(
                "response",
                "No response generated."
            )

        except Exception as error:

            return f"LLM Error: {str(error)}"
