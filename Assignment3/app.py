import pickle
from flask import Flask, request, jsonify
from score import score

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb")) # Load the trained model

@app.route('/', methods=['GET','POST'])
def get_score():
    if request.method=='POST':
        text = request.form['text']
        prediction, propensity = score(text, model, threshold=0.7)
        classification=['NOT SPAM','SPAM']
        response = {'prediction': prediction, 'propensity': propensity, 'Classification': classification[prediction]}
        return jsonify(response)      
    else:
        return """
            <!DOCTYPE html>
            <html lang="en">
            <body>
                <h1>SPAM Classification</h1>
                <form action="/" method="post">
                    <label for="text">Enter Text:</label><br>
                    <input type="text" id="text" name="text"><br><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
        """

app.run(debug=True)