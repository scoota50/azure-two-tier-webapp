
import os
import pymysql
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def get_db_connection():
    # Read the database password from the mounted Docker secret
    password_file = os.getenv("DB_PASSWORD_FILE")

    with open(password_file, "r", encoding="utf-8") as file:
        db_password = file.read().strip()

    # Connect to the MySQL database
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=db_password,
        database=os.getenv("DB_NAME"),
        connect_timeout=5
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
