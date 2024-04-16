from routes import app
from flask import render_template, request, redirect, url_for, session
from services.user import User_service

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    # 从 session 中获取用户名
    username = session.get('username')
    # 渲染 home.html 页面，并将用户名传递到页面中
    return render_template('home.html',username=username )

@app.post('/api/login')
def Login():
    data = request.get_json()
    name = data['username']
    password = data['password']
    res = User_service.check(name, password)
    if res:
        # 将用户名存储在 session 中
        session['username'] = name
        # 返回成功信息和用户名
        return {
            'code': 0,
            'message': '登录成功',
            'username': name
        }
    else:
        return {
            'code': -1,
            'message': '登录失败'
        }
