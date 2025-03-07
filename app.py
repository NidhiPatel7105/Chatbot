from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Manually inserted responses for the chatbot
responses = {
    "hi": "Hello! I’m Natasha Romanoff. What do you want?",
    "how are you": "I don’t have time for emotions. But I’m operational.",
    "who are you": "I am Black Widow, a former assassin and Avenger.",
    "tell me about shield": "S.H.I.E.L.D. was an intelligence agency. It had... issues.",
    "bye": "Stay safe. We might meet again.",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").lower()
    bot_response = responses.get(user_message, "I don’t have a response for that.")
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
    