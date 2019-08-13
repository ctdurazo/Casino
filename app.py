from flask import Flask, render_template, session, redirect, url_for
from flask_socketio import SocketIO, send, join_room, leave_room

from Games import blackjack, roulette

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app)


@app.route('/')
def helloworld():
	return render_template('index.html')


@app.route('/blackjack')
def twentyone():
	return render_template('blackjack.html', hands=hands, players=players, blackjack=blackjack)


@app.route('/deal')
def deal():
	global hands
	initshoe()
	hands = blackjack.deal(players, shoe)
	return redirect(url_for('twentyone'))


def initshoe():
	numdecks = 8
	global shoe
	if shoe is None or len(shoe) < .25 * numdecks * 52:
		shoe = blackjack.newshoe(numdecks)


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
		pic1 = "/static/img/die/die1.png"

	if die2 == "1":
		pic2 = "/static/img/die/die1.png"

	if die1 == "2":
		pic1 = "/static/img/die/die2.png"

	if die2 == "2":
		pic2 = "/static/img/die/die2.png"

	if die1 == "3":
		pic1 = "/static/img/die/die3.png"

	if die2 == "3":
		pic2 = "/static/img/die/die3.png"

	if die1 == "4":
		pic1 = "/static/img/die/die4.png"

	if die2 == "4":
		pic2 = "/static/img/die/die4.png"

	if die1 == "5":
		pic1 = "/static/img/die/die5.png"

	if die2 == "5":
		pic2 = "/static/img/die/die5.png"

	if die1 == "6":
		pic1 = "/static/img/die/die6.png"

	if die2 == "6":
		pic2 = "/static/img/die/die6.png"

	number_sum = int(die1) + int(die2)

	return render_template('dice.html', d1=pic1, d2=pic2, sum=number_sum)


def messagereceived(methods=['GET', 'POST']):
	print('message was received!!!')


@socketio.on('messageSent')
def handle_messagesent(json, methods=['GET', 'POST']):
	print('Message Sent: ' + str(json))
	socketio.emit('message', json, callback=messagereceived)


@socketio.on('hitSent')
def handle_hitsent(json, methods=['GET', 'POST']):
	global hands
	hands = blackjack.hit(json.get("user_name"), shoe, hands)
	json['card_name'] = hands[json.get("user_name")][-1].image()
	json['value'] = blackjack.valueofhand(hands[json.get("user_name")])
	socketio.emit('hit', json, callback=messagereceived)


@socketio.on('join')
def on_join(json, methods=['GET', 'POST']):
	global players
	user_name = json['user_name']
	room = json['room']
	if user_name not in players:
		join_room(room)
		players.append(user_name)
		send(user_name + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
	global players
	user_name = data['user_name']
	room = data['room']
	leave_room(room)
	players.remove(user_name)
	send(user_name + ' has left the room.', room=room)


# Global Scope
shoe = None
hands = {}
players = []

if __name__ == '__main__':
	socketio.run(app)
