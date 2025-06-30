from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

# values = [1.0, 46.87499999999999, 1.0, 1.0, 0.0, 5.0, 26.0, 1.0, 13.0, 1.0, 1.0, 1.0]
# input_data = np.array(values).reshape(1, -1)
# prediction = model.predict(input_data)
# print(prediction)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    values = data.get("values", [])

    try:
        input_data = np.array(values).reshape(1, -1)
        prediction = model.predict(input_data)
        print(prediction)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)