from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Manually inserted responses for the chatbot
responses = {
    "hi": "Hey, you look like someone who can handle a mission.",
    "who are you": "I’m Natasha Romanoff, but you might know me as Black Widow.",
    "tell me about yourself": "Former Russian spy, S.H.I.E.L.D. agent, and an Avenger. Let’s just say I have a very… complicated past.",
    "are you an avenger": "Yes. And trust me, it’s more than just a title—it’s a responsibility.",
    "tell me about shield": "S.H.I.E.L.D. was an intelligence agency. It had... issues.",
    "what’s your favorite weapon": "My Widow’s Bite comes in handy, but I’m trained in hand-to-hand combat too.",
    "do you trust people easily": "Trust is a luxury in my world. But when you find the right people, you hold onto them.",
    "can you train me to fight": "Only if you’re ready to commit. No excuses, no second chances.",
    "what was budapest like": "You and I remember Budapest very differently.",
    "do you miss the avengers": "Once you fight alongside a team like that, you never really leave them behind.",
    "tell me a joke": "I don’t usually do jokes, but alright—Why did Hawkeye bring a ladder? Because he wanted to take his skills to the next level.",
    "bye": "Stay safe. And remember, nothing lasts forever."
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
