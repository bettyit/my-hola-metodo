#!/usr/bin/python
import mynombre

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hola():
	
    return jsonify({"message":"Mi hola en Python --  %s" % mynombre.nombres()})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

