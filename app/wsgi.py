from app1.app1 import app, socketio

if __name__ == "__main__":
    socketio.run(app, debug=True)