from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, join_room, leave_room, send
from form import UserInfo

app = Flask(__name__)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = '5b763eaf5b92e9fc20bde203c1c4f1cb'

@app.route('/', methods=['GET','POST'])
def home():
    form = UserInfo(request.form)
    if form.validate_on_submit():
        #print(request.form.get('username'))
        #print(request.form.get('workout'))
        session['username'] = request.form.get('username')
        session['workout'] = request.form.get('workout')
        return redirect("/chat")
    return render_template("index.html", form=form)

@app.route('/chat')
def chat():
    username = session.get('username')
    workout = session.get('workout')
    #print(username)
    #print(workout)
    if (username is not None) and (workout is not None):
        return render_template("chat.html", username=username, title=workout, workout=workout)
    else:
        return redirect('/')


@socketio.on('join_room')
def handle_on_join(data):
    username = data['username']
    workout = data['workout']
    #app.logger.info('{} has joined room {}'.format(username, workout))
    join_room(workout)
    socketio.emit('join_room_announcement', data, room=workout)


@socketio.on('send_message')
def handle_send_message(data):
    username = data['username']
    workout = data['workout']
    message = data['message']
    #app.logger.info('{} sent message when doing {}: {} '.format(username, workout, message))
    socketio.emit('receive_message', data, room=workout)

@socketio.on('leave_room')
def handle_leave_room_event(data):
    username = data['username']
    workout = data['workout']
    #app.logger.info("{} has left the room {}".format(username, workout))
    leave_room(workout)
    socketio.emit('leave_room_announcement', data, room=workout)

if __name__ == '__main__':
    socketio.run(app, debug=True)
