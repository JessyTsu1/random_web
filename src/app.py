import argparse
import logging
import random

import numpy as np
import requests
from flask import Flask, Response, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    ('Task 1', 1),
    ('Task 2', 2),
    ('Task 3', 3),
]


@app.route('/random', methods=['GET'])
def random_index():
    random_list = np.random.rand(100000)

    ice_skating, badminton, skateboarding, programming, climbing, guitar, walk = [
        (random.choices(random_list)[0], name) for name in ["ice_skating", "badminton", "skateboarding", "programming", "climbing", "guitar", "walk"]
    ]
    max_item = max(ice_skating, badminton, skateboarding, programming, climbing, guitar, walk)

    return jsonify(f"we need to go：{max_item[1]}!", {"ice_skate": ice_skating,
                    "badminton": badminton,
                    "skateboarding": skateboarding,
                    "programming": programming,
                    "climbing": climbing,
                    "guitar": guitar,
                    "just walk": walk
                    }), 200


@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    weight = float(request.form['weight'])
    tasks.append((name, weight))
    return '', 204


@app.route('/delete', methods=['POST'])
def delete_task():
    task_id = int(request.form['id'])
    tasks.pop(task_id)
    return '', 204


@app.route('/edit', methods=['POST'])
def edit_task():
    task_id = int(request.form['id'])
    name = request.form['name']
    weight = float(request.form['weight'])
    tasks[task_id] = (name, weight)
    return '', 204



def get_log_level(args):
    if args.verbose == 2:
        return logging.INFO
    elif args.verbose > 2:
        return logging.DEBUG
    else:
        return logging.WARN


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BMInf Backend server")
    parser.add_argument("--debug", "-d", help="deploy debug mode",
                        action="store_true", default=False)
    parser.add_argument("--verbose", "-v", action="count", default=1)
    args = parser.parse_args()

    logging.basicConfig(level=get_log_level(
        args), format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

    if args.debug:
        app.run(debug=True, threaded=True, host='0.0.0.0', port=5000)
    else:
        app.run(debug=False, threaded=True, host='0.0.0.0', port=5000)
