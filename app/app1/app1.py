from flask import Flask, render_template
from flask import session
from flask_session import Session
from flask_socketio import SocketIO, emit
from flask import request
from uuid import uuid4
from Agent import Agent
from runner import *

app = Flask(__name__)
ag = Agent()
socketio = SocketIO(app)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
from flask import request
@app.route('/')
def home():
   return render_template('file.html')
if __name__ == '__main__':
   app.run()

@socketio.on('connect')
def connect():
    session['sid'] = request.sid

@socketio.on('press')
def press(message):
   global ag
   x = message['action']
   c1 = x//5
   c2 = x%5
   ag._mineFieldWorld[c1][c2]='M'
   print(x)

@socketio.on('play')
def play():
   print("heyo")
   global ag
   print(ag._mineFieldWorld)
   ans = main(ag)
   for i in ans:
      print("hey")
      socketio.emit('update_status',{"x":i[0],"y":i[1]},room=session['sid'])



