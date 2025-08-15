import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Gemini API Configuration ---
# Get the API key from the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the generative AI library
if not GEMINI_API_KEY:
    raise ValueError("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")

genai.configure(api_key=GEMINI_API_KEY)

# Use the gemini-1.5-flash-latest model
model = genai.GenerativeModel('gemini-1.5-flash-latest')
# --------------------------------

# --- Routes ---
@app.route('/')
def index():
    """Render the main chat page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle the chat request from the frontend."""
    try:
        # Get the user's message from the request
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Send message to Gemini and get the response
        response = model.generate_content(user_message)
        
        # Return the AI's response text
        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Failed to get a response from the AI."}), 500
# --------------

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)