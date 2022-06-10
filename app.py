import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)



# Add documentation here ---> 
@app.route('/')
def index():
    return render_template('index.html')


# Add documentation here ---> 
@app.route('/count-words', methods=['GET', 'POST'])
def count_words():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        f.seek(0)
        print("File saved")
        content = f.read()
        content = str(content, 'utf-8')
        words = content.split()
        result = len(words)
    return render_template("index.html", text=result)

if __name__ == '__main__':
    app.run(debug = True)