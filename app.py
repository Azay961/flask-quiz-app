from flask import Flask, render_template, request, session
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "Azay"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        action = request.form.get('action')

        if action == 'Check Answer':
            user_answer = request.form['option']
            if session["correct_answer"] == user_answer.strip():
                result = "Correct!"
            else:
                result = f"Incorrect. The correct answer is {session['correct_answer']}"
            return render_template('index.html', question=session["question"], option_a=session["option_a"], option_b=session["option_b"], option_c=session["option_c"], option_d=session["option_d"], result=result)
        
        elif action == 'Next Question':
            question, option_a, option_b, option_c, option_d, correct_answer = next_question()
            session["correct_answer"] = correct_answer
            session["question"] = question
            session["option_a"] = option_a
            session["option_b"] = option_b
            session["option_c"] = option_c
            session["option_d"] = option_d
            return render_template('index.html', question=question, option_a=option_a, option_b=option_b, option_c=option_c, option_d=option_d)

    else:
        question, option_a, option_b, option_c, option_d, correct_answer = next_question()
        session["correct_answer"] = correct_answer
        session["question"] = question
        session["option_a"] = option_a
        session["option_b"] = option_b
        session["option_c"] = option_c
        session["option_d"] = option_d
        return render_template('index.html', question=question, option_a=option_a, option_b=option_b, option_c=option_c, option_d=option_d)

def next_question():
    path = r'D:\my_projects\Flask_quiz_app\flask-quiz-app\Questions\Questions.csv'
    df = pd.read_csv(path).sample(1).iloc[0]
    question = df['Question']
    option_a = df['Option A']
    option_b = df['Option B']
    option_c = df['Option C']
    option_d = df['Option D']
    correct_answer = df['Correct Answer']

    return question, option_a, option_b, option_c, option_d, correct_answer

if __name__ == "__main__":
    app.run(debug=True)
