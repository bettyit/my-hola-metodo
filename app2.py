#!/usr/bin/python
import mynombre

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hola():
    return "Mi hola en Python --  %s\n" % mynombre.nombres()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
