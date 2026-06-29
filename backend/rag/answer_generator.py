import os
from openai import OpenAI
from backend.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful agriculture assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content