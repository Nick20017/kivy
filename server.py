import socketio
from aiohttp import web

server = socketio.AsyncServer(async_mode='aiohttp')

app = web.Application()

server.attach(app)

@server.on('connect')
def on_connected(sid, data):
    print('Connected')

@server.on('message')
async def on_message(sid, data):
    print('Socket ID: ', sid)
    print('Message: ', data)
    await server.emit('message', str.upper(data))

if __name__ == "__main__":
    web.run_app(app)