# AI Interview Screener (Backend Only)

A lightweight backend service built with **FastAPI** that evaluates and ranks candidate answers using **Groq LLM**.  
This project is designed as a **mini AI interview screener**, suitable for recruitment automation or skill assessment.
---
## Live API (Render Deployment)
https://ai-interview-screener.onrender.com

## API Documentation (Swagger)
https://ai-interview-screener.onrender.com/docs

---

## **Table of Contents**

1. [Features](#features)  
2. [Technology Stack](#technology-stack)  
3. [Project Structure](#project-structure)  
4. [Setup Instructions](#setup-instructions)  
5. [Environment Variables](#environment-variables)  
6. [Running the Server](#running-the-server)  
7. [API Endpoints](#api-endpoints)  
8. [Example Usage](#example-usage)  
9. [Best Practices](#best-practices)  
10. [Future Improvements](#future-improvements)  


---

## **Features**

- Evaluate a **single candidate answer** and get:
  - Score (1–5)
  - One-line summary
  - Suggested improvement

- Rank **multiple candidates** based on their answers

- Returns **clean JSON responses** for easy integration

- Lightweight, **fast**, and **backend-only** solution

---

## **Technology Stack**

- **FastAPI**: Python framework for building high-performance APIs  
- **Groq LLM**: AI evaluation of answers  
- **Python-dotenv**: Securely manage API keys  
- **Uvicorn**: ASGI server to run FastAPI applications  

**Why this stack?**  

- FastAPI allows fast API development and provides built-in **Swagger docs** at `/docs`  
- Groq LLM provides an open-source compatible AI model for evaluating candidate responses  
- Python-dotenv ensures **API keys are never pushed to GitHub**  

---

## **Project Structure**

```

ai-interview-screener/
├── app.py            # FastAPI endpoints
├── services.py       # AI evaluation logic
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
├── .gitignore        # Ignore .env and caches
└── .env              # Local environment variables (API keys)

````

---

## **Setup Instructions**

### 1. Clone the repository

```bash
git clone https://github.com/Harshanhkp24/ai-interview-screener-new.git
cd ai-interview-screener-new
````

### 2. Create a `.env` file (local only)

```
GROQ_API_KEY=your_groq_api_key_here
```

> **Important:** Never push `.env` to GitHub.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## **Running the Server**

```bash
uvicorn app:app --reload
```

* Visit **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Visit **OpenAPI JSON**: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## **API Endpoints**

### **1. Evaluate Answer**

* **URL:** `/evaluate-answer`
* **Method:** POST
* **Request Body:**

```json
{
  "answer": "I improved website speed by optimizing database queries."
}
```

* **Response:**

```json
{
  "score": 4,
  "summary": "Good optimization of backend queries improved performance",
  "improvement": "Provide metrics to quantify the improvement"
}
```

---

### **2. Rank Candidates**

* **URL:** `/rank-candidates`
* **Method:** POST
* **Request Body:**

```json
{
  "answers": [
    "Answer 1",
    "Answer 2",
    "Answer 3"
  ]
}
```

* **Response:** Sorted array by score (highest first)

```json
[
  {
    "score": 5,
    "summary": "Excellent answer with measurable impact",
    "improvement": "Provide additional context if possible"
  },
  {
    "score": 3,
    "summary": "Average explanation",
    "improvement": "Be more specific"
  }
]
```

---

## **Best Practices**

* Always store API keys in `.env`
* Use `.gitignore` to avoid pushing secrets
* Validate Groq API key before running the server
* Use JSON schema to ensure client apps parse responses correctly

---

## **Future Improvements**

* Add **authentication** to API endpoints
* Include **multi-language support** for candidate answers
* Build a **frontend dashboard** to visualize scores
* Support **customizable scoring rubrics** per company needs


