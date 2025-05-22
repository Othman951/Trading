import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_market(pairs):
    prompt = f"Analyse les données suivantes : {pairs}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
