import requests


class APILLM:

    def __init__(
        self,
        api_key,
        model="gpt-4o-mini",
        base_url="https://api.openai.com/v1/chat/completions"
    ):

        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    def generate_answer(
        self,
        query,
        context
    ):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        prompt = f"""
You are an academic assistant.

Answer only from the provided context.

If the answer is not available in the context,
respond with:

'I could not find the answer in the uploaded documents.'

Context:
{context}

Question:
{query}
"""

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2
        }

        try:

            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            result = response.json()

            return result["choices"][0]["message"]["content"]

        except Exception as error:

            return f"API Error: {str(error)}"
