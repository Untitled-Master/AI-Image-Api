from flask import Flask, request, jsonify
import replicate

app = Flask(__name__)


@app.route('/generate_image', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        if not data or 'input' not in data:
            return jsonify({"error": "Invalid input data"}), 400

        input_data = data['input']

        output = replicate.run(
            "adirik/realvisxl-v3.0-turbo:6e941e7fe46955afc031f35e84312a792d546b0f434f9008d457eb9deb24575c",
            input=input_data
        )

        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
