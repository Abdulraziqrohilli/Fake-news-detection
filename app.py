from flask import Flask, render_template, request
import joblib

# Load the saved model and vectorizer
model = joblib.load('fake_news_detector.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the news text from the form
        news_text = request.form['news_text']

        # Transform the input text using the vectorizer
        news_tfidf = vectorizer.transform([news_text])

        # Make a prediction using the model
        prediction = model.predict(news_tfidf)

        # Map the prediction to a human-readable label
        result = "Fake News" if prediction[0] == 1 else "Real News"

        # Render the result in the template
        return render_template('index.html', prediction_text=f'The news is: {result}')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)