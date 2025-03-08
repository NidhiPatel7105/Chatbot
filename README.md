🗣️ Persona Chatbot

A simple web-based chatbot built using Flask and JavaScript, where responses are manually inserted to create a custom personality.

🚀 Features

✅ Custom Responses – Define your own chatbot personality

✅ Flask Backend – Handles user input and chatbot responses

✅ Interactive UI – Simple chat interface using HTML, CSS, and JavaScript

✅ Easy to Modify – Expand response dictionary or use a database


🛠 Installation & Setup

1️⃣ Clone the Repository

bash

Copy

Edit

git clone https://github.com/NidhiPatel7105/Chatbot.git

cd persona-chatbot

2️⃣ Install Dependencies

Ensure you have Python and Flask installed:

bash

Copy

Edit

pip install flask

3️⃣ Run the Flask Server

bash

Copy

Edit

python app.py

4️⃣ Open in Browser

Visit http://127.0.0.1:5000/ to chat with the bot.

📂 Project Structure

bash

Copy

Edit

/persona-chatbot
├── app.py                 # Flask backend
├── /templates
│   ├── index.html         # Chatbot UI
└── README.md              # Project documentation

⚡ How It Works

The chatbot matches user messages with predefined responses stored in a Python dictionary.

If a message isn't found, the bot replies with a default response.

The frontend (HTML, CSS, JavaScript) sends user messages to the Flask backend via AJAX.

✨ Customizing Responses

Modify responses in app.py to change chatbot replies:

python

Copy

Edit

responses = {
    "hi": "Hello there!",
    "how are you": "I'm doing great, thank you!",
    "bye": "Goodbye! Have a great day!",
}

🔥 Future Enhancements

🔹 Store responses in a database

🔹 Add user authentication

🔹 Support multiple chatbot personalities

📜 License

This project is open-source. Feel free to modify and improve it! 🚀

