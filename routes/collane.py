# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json
from contextlib import closing

import psycopg2
from flask import Response

import utils.database


def get_collane():
    data = []

    try:
        db = utils.database.get_db()

        with closing(db.cursor()) as cur:
            cur.execute("SELECT id_collana, nome FROM collane ORDER BY nome")
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    except psycopg2.OperationalError:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp
