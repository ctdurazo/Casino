from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, send

from Games import blackjack, roulette

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
	for i in range(0, numplayers - 1):
		out = out + '<p><img src="/static/img/cards/' + hands[i]['cards'][0].image() + '"/>, ' \
			+ '<img src="/static/img/cards/' + hands[i]['cards'][1].image() + '"/> = ' \
			+ str(blackjack.valueofhand(hands[i]['cards'])) + '</p>'
	out = out + '<p><img src="/static/img/cards/' + hands[numplayers - 1]['cards'][0].image() + '"/>, , ' \
		+ '<img src="/static/img/cards/gray_back.png"/>  =' \
		+ str(hands[numplayers - 1]['cards'][0].value(0)) + '</p>'
	return out


@app.route('/roulette')
def wheelroulette():
	number = roulette.generate_number(0, 37)
	even_or_odd = roulette.isEvenOrOdd(number)
	color = roulette.getColor(number)

	if color == "red":
		if even_or_odd == "even":
			return render_template('red_even.html', number=number)
		elif even_or_odd == "odd":
			return render_template('red_odd.html', number=number)
		else:
			return render_template('red_neither.html', number=number)
	elif color == "black":
		if even_or_odd == "even":
			return render_template('black_even.html', number=number)
		elif even_or_odd == "odd":
			return render_template('black_odd.html', number=number)
		else:
			return render_template('black_neither.html', number=number)
	# color is green
	else:
		return render_template('green.html', number=number)


@app.route('/dice')
def dice():
	die1 = roulette.generate_number(1, 6)
	die2 = roulette.generate_number(1, 6)
	pic1 = ''
	pic2 = ''

	if die1 == "1":
		pic1 = "/static/die1.png"

	if die2 == "1":
		pic2 = "/static/die1.png"

	if die1 == "2":
		pic1 = "/static/die2.png"

	if die2 == "2":
		pic2 = "/static/die2.png"

	if die1 == "3":
		pic1 = "/static/die3.png"

	if die2 == "3":
		pic2 = "/static/die3.png"

	if die1 == "4":
		pic1 = "/static/die4.png"

	if die2 == "4":
		pic2 = "/static/die4.png"

	if die1 == "5":
		pic1 = "/static/die5.png"

	if die2 == "5":
		pic2 = "/static/die5.png"

	if die1 == "6":
		pic1 = "/static/die6.png"

	if die2 == "6":
		pic2 = "/static/die6.png"

	number_sum = int(die1) + int(die2)

	return render_template('dice.html', d1=pic1, d2=pic2, sum=number_sum)


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
