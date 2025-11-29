import os
import json
from groq import Groq 
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def evaluate_answer_llm(answer: str):
    prompt = f"""
You are a professional AI interview screener.

Evaluate the candidate’s answer.

Answer: {answer}

Return JSON with:
- score: number from 1 to 5
- summary: one-line summary of the answer
- improvement: one improvement suggestion

Respond ONLY with valid JSON. No extra text.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You evaluate candidate answers."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3
    )

    ai_text = response.choices[0].message.content

    # Always attempt strict JSON parsing
    try:
        return json.loads(ai_text)
    except:
        # Fallback — in case model returns something weird
        return {
            "score": 3,
            "summary": "Model did not return valid JSON",
            "improvement": "Ensure strict formatting"
        }
