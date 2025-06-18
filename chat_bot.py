from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "qwen3:0.6b"

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")
    response = ask_ollama(user_input)
    return jsonify({"response": response})

def ask_ollama(prompt):
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful and friendly chatbot. "
                        "Respond to the user naturally. DO NOT explain your reasoning. "
                        "Just give the final reply as if you're a person chatting. "
                        "Each response should be short and conversational. No analysis. No meta-thinking."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
        res = requests.post(OLLAMA_URL, json=payload)
        res.raise_for_status()
        data = res.json()
        # Show only the last line of the response
        return data["message"]["content"].strip().splitlines()[-1]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
