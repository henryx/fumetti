# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json
from contextlib import closing

import psycopg2
from flask import Response, request

import utils.database


class Serie:
    def __init__(self):
        pass

    def request_serie(self):
        if request.method == "GET":
            resp = self.get_serie()
        elif request.method == "POST":
            resp = self.post_serie()
        else:
            res = {"msg": "Request not allowed", "op": "ko"}
            resp = Response(json.dumps(res), status=405, mimetype="application/json")

        return resp

    def get_serie(self):
        data = []

        try:
            db = utils.database.get_db()

            with closing(db.cursor()) as cur:
                cur.execute("SELECT id_serie, nome FROM serie ORDER BY nome")
                results = cur.fetchall()
                for item in results:
                    data.append({"id": item[0], "name": item[1]})

            res = {"data": data, "op": "ok"}
            resp = Response(json.dumps(res), status=200, mimetype="application/json")
        except psycopg2.OperationalError:
            res = {"op": "ko", "msg": "Error to connect to database"}
            resp = Response(json.dumps(res), status=500, mimetype="application/json")

        return resp

    def post_serie(self):
        content = request.get_json("data")
        # TODO: check if serie exists (act a lowercase for name?)

        if utils.database.insert_serie(utils.database.get_db(), content):
            res = {"data": content, "op": "ok"}
            resp = Response(json.dumps(res), status=200, mimetype="application/json")
        else:
            res = {"op": "ko", "msg": "Error to connect to database"}
            resp = Response(json.dumps(res), status=500, mimetype="application/json")

        return resp
