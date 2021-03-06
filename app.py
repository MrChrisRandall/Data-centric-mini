import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://chris1605:Chrisrandall91@myfirstcluster-sn6xx.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def hello():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
