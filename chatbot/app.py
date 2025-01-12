from flask import Flask, request, jsonify
import threading

# Initialiser l'application Flask
app = Flask(__name__)

# Ajouter une route pour le chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    # Logique simple pour répondre au message
    if "buy" in user_message.lower():
        response = "The strategy suggests buying when VIX is below its moving average."
    elif "sell" in user_message.lower():
        response = "The strategy suggests selling when the price is 10% higher or 5% lower than the entry price."
    elif "result" in user_message.lower():
        response = f"The total return of the backtesting is {total_return:.2f}%."
    else:
        response = "I can help you with 'buy', 'sell', or 'result'."

    return jsonify({"response": response})

# Fonction pour lancer le serveur Flask dans un thread séparé
def run_flask():
    app.run(port=5000)

# Lancer le serveur Flask
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()
