import socketio

client = socketio.Client()
client.connect('http://localhost:8080')

@client.on('connect')
def connect():
    print("Connected")

@client.on('message')
def message(data):
    print(data)

while(True):
    message = input("Enter message: ")
    if message is None:
        break
    client.emit('message', message)