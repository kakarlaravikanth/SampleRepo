import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    return str(cursor.fetchall())


@app.route("/run")
def run_command():
    command = request.args.get("cmd")
    return os.popen(command).read()


password = "HardcodedAdminPassword123"
