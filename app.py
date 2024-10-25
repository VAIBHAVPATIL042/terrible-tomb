from flask import Flask, render_template, request, jsonify
from groq import Groq  # Make sure this is the correct import path
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize the Groq API client
client = Groq(api_key="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")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Send message to the Groq API and get response
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_message}],
        model="llama3-8b-8192",
    )
    
    response = chat_completion.choices[0].message.content
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
