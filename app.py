from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        return "ddd"
    else:
        return render_template("search.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)
