from flask import Flask, request, render_template
import pickle
from text import TextSummarizer

app = Flask(__name__)

# Load the TextSummarizer object from the pickle file
with open('textsummarizer.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def short():
    text = str(request.form.get('text', 'none'))
    percentage = float(request.form.get('percentage', '0')) / 100

    summary, ol, sl = model.summarize_text(text, percentage)

    return render_template('index.html', result=summary,original_text=text,original_length=ol,summary_length=sl)

if __name__ == '__main__':
    app.run(debug=True)
