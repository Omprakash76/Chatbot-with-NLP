from flask import Flask,render_template
from flask_socketio import  SocketIO,emit

app = Flask(__name__)

app.config['SECRET_KEY'] ='mynameharish'
socketio= SocketIO(app)


@app.route('/')
def index():
    return render_template('/chating.html')

if __name__ == '__main__':
    socketio.run(app,debug=True)