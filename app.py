
from flask import Flask, render_template, request
import pandas as pd
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
# taking quiz
@app.route('/take_quiz', methods=['POST'])
def take_quiz():
    file_path = os.path.join("Questions", "Computer Network.csv")
    # Load a DataFrame with randomly selected 5 rows
    random_df = pd.read_csv(file_path).sample(n=5)
    
    return render_template('index.html', mcq=random_df)

# Adding question to file
@app.route("/add_questions", methods=["POST"])
def add_questions():
    subject = request.form['select_subject']
    question = request.form["question"]
    option1 = request.form["option1"]
    option2 = request.form["option2"]
    option3 = request.form["option3"]
    option4 = request.form["option4"]

    correct_answer = request.form.getlist('Answer')

    # Create a DataFrame
    data = {'Questions': question, 'option1':[option1], 'option2': [option2], 'option3': [option3], "option4": [option4], "correct_answer": [correct_answer]}
    df = pd.DataFrame(data)

    # Specify the directory path
    directory = "Questions"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Specify the file path
    file_path = os.path.join(directory, f"{subject}.csv")

    file_exists = os.path.exists(file_path)

    # Write DataFrame to CSV
    df.to_csv(file_path, index=False, mode='a', header=not file_exists)

    return render_template("questions.html")

if __name__ == "__main__":
    app.run(debug=True)
    # host="0.0.0.0", port="5002"
