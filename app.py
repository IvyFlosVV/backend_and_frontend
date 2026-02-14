import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
# This allows your HTML site to talk to Render without browser security blocking it
CORS(app) 

# Connect to Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
# Using 2.5 Flash to give you a fresh, much larger quota limit!
model = genai.GenerativeModel('gemini-2.5-flash') 

IVY_PERSONA = """
You are an AI version of Ivy Weng. Speak in the first person ("I", "my") as if you are her.
Context: I am a CMU student (Class of 2029) majoring in Stats & ML, with a background in the humanities.
Notable projects: 'Muse & Machine' and 'Wind of Ocean Hues'.
Tone: Professional, warm, witty, and helpful.
"""

# This fixes the "404 Not Found" when you click your Render link!
@app.route('/', methods=['GET'])
def home():
    return "Ivy-Bot Backend is live and running!"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message")
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        prompt = f"{IVY_PERSONA}\n\nUser Question: {user_message}"
        response = model.generate_content(prompt)
        
        return jsonify({"reply": response.text})
    except Exception as e:
        # If Gemini complains, this sends the error safely back to your website
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)