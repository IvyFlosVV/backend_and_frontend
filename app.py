import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # Crucial: allows your portfolio to talk to Render

# Setup Gemini using the environment variable you just set on Render
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash-lite')

IVY_PERSONA = """
You are Ivy-Bot, an AI version of Ivy Weng. 
Context: CMU student (Class of 2029), Stats & ML major, background in humanities.
Notable projects: 'Muse & Machine' and 'Wind of Ocean Hues'.
Tone: Professional, warm, and witty (Retro Warm aesthetic).
"""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        prompt = f"{IVY_PERSONA}\n\nUser Question: {user_message}"
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)