from fastapi import FastAPI
from pydantic import BaseModel
from services import evaluate_answer_llm

app = FastAPI()

class EvaluateRequest(BaseModel):
    answer: str

class RankRequest(BaseModel):
    answers: list[str]

@app.post("/evaluate-answer")
async def evaluate_answer(data: EvaluateRequest):
    return await evaluate_answer_llm(data.answer)

@app.post("/rank-candidates")
async def rank_candidates(data: RankRequest):
    results = []
    for ans in data.answers:
        result = await evaluate_answer_llm(ans)
        results.append(result)

    ranked = sorted(results, key=lambda x: x["score"], reverse=True)
    return ranked
