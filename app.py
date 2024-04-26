from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/computer_organization', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get("input_text")

   
        return render_template('index.html', query=query, results=query)

        

if __name__ == "__main__":
    app.run(debug=True)