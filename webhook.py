from flask import Flask, request
from firebase import main as firebase_main

app = Flask(__name__)

@app.route('/webhook-k9lx22t5-77', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        firebase_main(payload, 'webhook-k9lx22t5-77')
        body = request.get_data(as_text=True)
        app.logger.info("Request body: {}".format(body))
        return 'OK', 200
    else:
        return 'Bad Request', 400

if __name__ == '__main__':
    app.run()