from flask import Flask, render_template

app = Flask(__name__)

#main
@app.route('/')
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()