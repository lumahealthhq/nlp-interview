from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_swagger import swagger
from sentiment_server import SentimentService
from cnn_text import CNN_Text


app = Flask(__name__)


@app.route('/')
def index():
    return 'Sentiment API, go to /docs for swagger'


@app.route('/sentiment', methods=['POST'])
def sentiment_check():
    """
        Makes a sentiment analysis
        ---
        
        parameters:
          - in: body
            name: body
            properties:
                text:
                  type: string
                  description: text to be evaluated             

        responses:
          200:
            description: positive, negative or neutral
        """
    text = request.get_json()['text']
    service = SentimentService()
    resp = service.predict(text)
    return jsonify(resp)

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Sentiment API"
    return jsonify(swag)

app.register_blueprint(
    get_swaggerui_blueprint('/docs','http://localhost:5000/spec'),url_prefix='/docs')

if __name__ == "__main__":
    app.run()