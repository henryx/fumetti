# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json

from flask import Response, request

from utils import database


class Albi:
    def __init__(self):
        pass

    def get_albi(self, serie=None):
        # TODO: returns all albi for requested serie

        res = {"msg": "GET albi for <{0}> requested".format(serie), "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
        return resp

    def post_albi(self):
        content = request.get_json("data")

        if database.insert_albo(database.get_db(), content):
            res = {"msg": "Saved albo successfully", "op": "ok"}
            status = 200
        else:
            res = {"msg": "An error was occurred when saving albo", "op": "ko"}
            status = 500

        resp = Response(json.dumps(res), status=status, mimetype="application/json")
        return resp
