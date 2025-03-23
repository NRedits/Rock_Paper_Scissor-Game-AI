from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

winning_moves = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}
ai_score = 0
player_score = 0

def get_ai_move():
    return random.choice(['Rock', 'Paper', 'Scissors'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_game():
    global ai_score, player_score
    player_choice = request.json['choice']
    ai_choice = get_ai_move()

    if player_choice == ai_choice:
        result = "It's a Draw! 🤝"
    elif winning_moves[player_choice] == ai_choice:
        player_score += 1
        result = "You Win! 🎉"
    else:
        ai_score += 1
        result = "AI Wins! 🤖"

    return jsonify({'ai_choice': ai_choice, 'result': result, 'player_score': player_score, 'ai_score': ai_score})

if __name__ == '__main__':
    app.run(debug=True)
