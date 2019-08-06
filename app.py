from flask import Flask
from Games import blackjack

app = Flask(__name__)


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
	for i in range(0, numplayers):
		out = out + '<p>' + hands[i]['cards'][0].description() + ', ' \
		+ hands[i]['cards'][1].description() + ' = ' \
		+ str(blackjack.valueofhand(hands[i]['cards'])) + '</p>'
	return out


if __name__ == '__main__':
	app.run()
