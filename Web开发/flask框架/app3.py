from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/msgmsgmsg', methods=['POST'])
def process_json():
    if request.method == 'POST':
        # 假设收到的是 JSON 格式的数据
        data = request.get_data(as_text=True)
        return data

    else:
        return "Only POST requests are allowed for this endpoint"


if __name__ == '__main__':
    app.run(debug=True)
