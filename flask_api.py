from flask import Flask, request, jsonify
import pickle
from model_utils import is_even_model

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    number = int(data.get("number", 0))
    prediction = model(number)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(port = 5000)