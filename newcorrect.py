from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__, template_folder='/home/teslalary/templates')
# 在这一行启用CORS
cors = CORS(app)

@app.route('/')
def home():
    resp = make_response(render_template('qianduan.html'))
    resp.headers['Referrer-Policy'] = 'no-referrer'
    return resp

@app.route('/compute/<int:num1>/<int:num2>')
@cross_origin()  # 允许所有域名跨域请求这个路由
def compute(num1, num2):
    return str(num1 * num2)

@app.route('/equation/start', methods=['GET'])
@cross_origin()  # 允许所有域名跨域请求这个路由
def start():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    return {'num1': num1, 'num2': num2, 'num3': num3}

@app.route('/botanswer/return', methods=['POST'])
@cross_origin()  # 允许所有域名跨域请求这个路由
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
    app.run(host='localhost', port=5001)
