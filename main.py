from flask import Flask, render_template, json, jsonify, request

app = Flask(__name__)

@app.route("/")
@app.route("/chat")

def index():
  return render_template('chat.html')

@app.route('/chat/read')
def ielasit_chatu():
  chata_rindas = []
  with open("chatlog.txt", "r", encoding="UTF-8") as f:
    for rinda in f:
      chata_rindas.append(rinda)
  return jsonify({"chats": chata_rindas})

@app.route('/chat/send', methods=['POST'])
def send_message():
  dati = request.json
  
  with open("chatlog.txt", "a", newline="", encoding="UTF-8") as f:
    f.write(dati["chats"] + "\n")

  return ielasit_chatu()
  
if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5000, debug=True)