

# import flask library
# import textblob library

from flask import Flask, render_template, request
from textblob import TextBlob


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        text = str(request.form['text'])

        blob = TextBlob(text)
        analyze = 0

        for sentence in blob.sentences:
            print(sentence.sentiment)

            analyze= sentence.sentiment
        return render_template('text.html', text=text, score=analyze)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


