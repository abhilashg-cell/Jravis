import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma2:latest"

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
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)
        result = response.json()

        raw_reply = result.get("response", "").strip()

        # Extract JSON safely
        start = raw_reply.find("{")
        end = raw_reply.rfind("}") + 1
        json_text = raw_reply[start:end]

        parsed = json.loads(json_text)

        return parsed.get("response", "I could not understand that.")

    except Exception as e:
        print(f"[OLLAMA ERROR]: {e}")
        return "Sorry sir, I encountered an error."