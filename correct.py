"""批改机：随机生成等式，需要学生来模仿老师一样来批改作业
此为python单程序版本，效果差不多就是这样，
还需要做一个flask应用，来做前后端分离，
部署到pythonanywhere上方便随时使用
"""

import random


def generate_equation():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ture_result =  num1 * num2
    false_result = random.randint(1, 10)
    equation = f"{num1} * {num2} = {false_result}"
    return equation

def validate_answer(equation, answer):
    """真实正确的机器答案"""
    true_result = eval(equation.split('=')[0].strip())
    if int(answer) == true_result:
        return True
    else:
        return False

def main():
    equation = generate_equation()
    print("请判断以下等式是否正确：")
    print(equation)

    user_choice = input("是否选择“对”？(Y/N)")
    if user_choice.upper() == "Y":
        bot_result = eval(equation.split('=')[0].strip())
        if bot_result == int(equation.split('=')[1].strip()):
            print("选择正确！")
        else:
            print("选择错误！")
    else:
        user_answer = input("请输入您的答案：")
        if validate_answer(equation, user_answer):
            print("答案正确！")
        else:
            print("答案错误！")

    user_choice = input("是否查看机器计算的正确结果？(Y/N)")
    if user_choice.upper() == "Y":
        result = eval(equation.split('=')[0].strip())
        print(f"机器计算的正确结果为：{result}")

if __name__ == "__main__":
    main()

