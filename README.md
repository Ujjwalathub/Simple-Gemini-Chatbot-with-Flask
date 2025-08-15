Simple Gemini Chatbot with FlaskA lightweight and straightforward web-based chatbot powered by Google's Gemini API and built with the Python Flask framework.This project provides a minimal user interface to send messages and receive real-time responses from the gemini-1.5-flash-latest model. The backend is handled by a Flask server that securely manages the API key, communicates with the Gemini API, and serves the frontend.FeaturesSimple Backend: A clean Flask application that exposes a /chat endpoint to handle user messages.AI Integration: Seamlessly integrates with the Google Gemini API to generate intelligent and contextual responses.Secure API Key Handling: Uses a .env file to securely manage your Gemini API key, keeping it out of your source code.Basic Frontend: Includes a simple index.html with JavaScript to interact with the chatbot.Easy to Run: Designed for easy local setup and development.PrerequisitesBefore you begin, ensure you have the following installed:Python 3.8+pip (Python package installer)A Google Gemini API Key. You can get one from Google AI Studio.Installation & SetupFollow these steps to get your local development environment set up and running.1. Clone the repository:git clone <your-repository-url>
cd <your-repository-name>
2. Create and activate a virtual environment:Windows:python -m venv venv
.\venv\Scripts\activate
macOS / Linux:python3 -m venv venv
source venv/bin/activate
3. Install the required packages:Create a requirements.txt file with the following content:Flask
google-generativeai
python-dotenv
Then, run this command to install them:pip install -r requirements.txt
4. Set up your environment variables:Create a file named .env in the root of your project directory and add your Gemini API key:GEMINI_API_KEY="YOUR_API_KEY_HERE"
Important: Remember to add .env to your .gitignore file to prevent your API key from being committed to version control.UsageOnce the setup is complete, you can run the Flask application with the following command:python app.py
The application will start on http://127.0.0.1:5000. Open this URL in your web browser to start chatting with the bot.File Structure.
├── venv/
├── templates/
│   └── index.html      # Frontend HTML and JavaScript
├── .env                # Stores environment variables (API key)
├── app.py              # Main Flask application logic
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
LicenseThis project is licensed under the MIT License. See the LICENSE file for details.
