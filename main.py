from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
from form import UserInfo

app = Flask(__name__)
app.config['SECRET_KEY'] = '5b763eaf5b92e9fc20bde203c1c4f1cb'

@app.route('/', methods=['GET','POST'])
def home():
    form = UserInfo()
    if form.validate_on_submit():
        print("success")
    return render_template("index.html", form=form)

@app.route('/chat')
def chat():
    username = request.args.get('username')
    if username:
        return render_template("chat.html", username=username)
    else:
        redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
