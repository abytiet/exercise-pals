from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO
from form import UserInfo

app = Flask(__name__)
app.config['SECRET_KEY'] = '5b763eaf5b92e9fc20bde203c1c4f1cb'

@app.route('/', methods=['GET','POST'])
def home():
    form = UserInfo(request.form)
    if form.validate_on_submit():
        print(request.form.get('username'))
        session['username'] = request.form.get('username')
        return redirect("/chat")
    return render_template("index.html", form=form)

@app.route('/chat')
def chat():
    username = session.get('username')
    print(username)
    if username is not None:
        return render_template("chat.html", username=username)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
