from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
# 在这一行启用CORS
CORS(app)

def compute(num1, num2):
    return num1 * num2

@app.route('/equation/start', methods=['GET'])
def start():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    return {'num1': num1, 'num2': num2, 'num3': num3}

@app.route('/botanswer/return', methods=['POST'])
def check():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    num3 = data.get('num3')
    userRight = data.get('userRight')  # 获取用户的判断
    computing = num1 * num2
    computingresult = True if computing == num3 else False
    result = True if userRight == computingresult else False
    return jsonify(computing=computing,result=result)




if __name__ == '__main__':
    app.run(host='localhost', port=5000)