
from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('questions.html')

@app.route('/take_quiz', methods=['POST'])
def predict_sentiment():
    input_text = request.form['input_text']
    subject = request.form['model_dropdown']
    if subject == "Computer Network":
        df = pd.read_csv(r'D:\my_projects\Flask_quiz_app\flask-quiz-app\Questions\computer_network.csv')
    
    return render_template('index.html')

# Adding question to file
@app.route("/add_questions", methods=["POST"])
def add_questions():
    subject = request.form['select_subject']
    question = request.form["question"]
    option1 = request.form["option1"]
    option2 = request.form["option2"]
    option3 = request.form["option3"]
    option4 = request.form["option4"]
    correct_answer = request.form["correct_answer"]

    # Create a DataFrame
    data = {'Questions': question, 'option1': option1, 'option2': option2, 'option3': option3, "option4": option4, "correct_answer": correct_answer}
    df = pd.DataFrame(data)

    # Save DataFrame to CSV
    file_path = f"/Questions/{subject}.csv"
    df.to_csv(file_path, mode='a', index=index, header=False)

    render_template("questions.html")

if __name__ == "__main__":
    app.run(debug=True)
    # host="0.0.0.0", port="5002"
