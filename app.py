
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

@app.route("/add_questions", methods=["POST"])
def add_questions():
    subject = request.form['model_dropdown']
    render_template("questions.html")

if __name__ == "__main__":
    app.run(debug=True)
    # host="0.0.0.0", port="5002"
