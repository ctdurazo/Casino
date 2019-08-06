from flask import Flask
from flask_socketio import SocketIO, send

from Games import blackjack

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app)


@app.route('/')
def helloworld():
	return 'Hello World'


@app.route('/blackjack')
def twentyone():
	numdecks = 4
	numplayers = 3
	deck = blackjack.newdeck(numdecks)
	hands = blackjack.deal(numplayers, deck)
	out = ''
	for i in range(0, numplayers-1):
		out = out + '<p>' + hands[i]['cards'][0].description() + ', ' \
			+ hands[i]['cards'][1].description() + ' = ' \
			+ str(blackjack.valueofhand(hands[i]['cards'])) + '</p>'
	out = out + '<p>' + hands[numplayers-1]['cards'][0].description() + ', ' \
		+ str(hands[numplayers-1]['cards'][0].value(0)) + '</p>'
	return out


def messagereceived(methods=['GET', 'POST']):
	print('message was received!!!')


@socketio.on('messageSent')
def handle_messagesent(json, methods=['GET', 'POST']):
	print('Message Sent: ' + str(json))
	socketio.emit('message', json, callback=messagereceived)


@socketio.on('message')
def handle_message(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)


if __name__ == '__main__':
	socketio.run(app)
