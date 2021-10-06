from flask import Flask, jsonify, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=["POST"])
def translate():
    request_data = request.get_json()
    q = request_data["q"]
    source = request_data["source"]
    target = request_data["target"]

    if( source == "" ):
        translatedObj = translator.translate(q, dest=target)
    else :
        translatedObj = translator.translate(q, dest=target, src=source)

    #print(translator.translate('veritas lux mea', src='la'))
    response = {"translatedText": translatedObj.text}
    return response


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port="3000")
