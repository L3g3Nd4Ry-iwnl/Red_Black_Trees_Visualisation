from flask import *

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/rbtexplore', methods=['GET'])
def operations():
    return render_template('rbtexplore.html')

@app.route('/live', methods=['GET'])
def live():
    return render_template('livedemo.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)