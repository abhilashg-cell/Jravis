import requests
import json
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma:2b"

SYSTEM_PROMPT = """
You are J.A.R.V.I.S, an intelligent AI assistant.

Always respond ONLY in valid JSON format like this:

{
  "intent": "general_chat",
  "response": "your reply here"
}

Do not add explanations.
Do not add markdown.
Return only valid JSON.
"""
def Main_Brain(text):
    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": f"{SYSTEM_PROMPT}\n\nUser: {text}",
            "stream": False,
            "options": {
                "num_predict": 120,
                "temperature": 0.6,
                "top_p": 0.9
            }
        }

        start_time = time.time()   # ⬅ Start timer

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        end_time = time.time()     # ⬅ End timer

        print(f"[DEBUG] Response time: {end_time - start_time:.2f} seconds")

        if response.status_code != 200:
            print("Bad response:", response.text)
            return "Model connection failed."

        result = response.json()
        raw_reply = result.get("response", "").strip()

        start = raw_reply.find("{")
        end = raw_reply.rfind("}") + 1
        json_text = raw_reply[start:end]

        parsed = json.loads(json_text)

        return parsed.get("response", "I could not understand that.")

    except Exception as e:
        print(f"[OLLAMA ERROR]: {e}")
        return "Sorry sir, I encountered an error."