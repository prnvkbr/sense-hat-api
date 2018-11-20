from flask import Flask, render_template, jsonify
from app.src.sense_hat import Hat

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get', methods=['GET'])
def get():
    result = Hat.get_data()
    print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
