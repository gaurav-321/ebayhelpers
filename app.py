import os
import threading
from flask import Flask, redirect, url_for, render_template, request
from main import query_obj
from flask_apscheduler import APScheduler


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'main:query_obj.find_products',
            'args': (),
            'trigger': 'interval',
            'seconds': 30
        }
    ]

    SCHEDULER_API_ENABLED = True


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = os.urandom(12).hex()
app.config.from_object(Config())


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        query_obj.add(query)
        return redirect("/directory")
    else:
        return render_template("search.html")


@app.route("/directory", methods=['GET'])
def directory():
    data_list = []
    if len(query_obj.searches) > 0:
        for index, query in enumerate(query_obj.searches):
            data_list.append([index, query[0], len(query[1])])
    return render_template("directory.html", data_list=data_list)


@app.route("/products", methods=['GET'])
def products():
    query_id = request.args.get("id")
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")
    list_data = query_obj.searches[int(query_id)][1]
    if min_price:
        list_data = [x for x in list_data if float(x[4])  > int(min_price)]
    if max_price:
        list_data = [x for x in list_data if float(x[4]) < int(max_price)]
    return render_template("products.html", list_data=list_data)


if __name__ == '__main__':
    scheduler = APScheduler()
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()
    app.run(host="127.0.0.1", port=80, debug=True, threaded=True, use_reloader=False)
