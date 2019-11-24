# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
import json
from contextlib import closing

import psycopg2
from flask import Response

import utils


def execute_query_lookup(query):
    data = []

    try:
        db = utils.database.get_db()

        with closing(db.cursor()) as cur:
            cur.execute(query)
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

        res = {"data": data, "op": "ok"}
    except psycopg2.OperationalError:
        res = {"op": "ko", "msg": "Error to connect to database"}

    return res


def get_valuta():
    query = "SELECT id_valuta, simbolo FROM valuta"

    res = execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_rilegatura():
    query = "SELECT id_rilegatura, descrizione FROM rilegatura"

    res = execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_conservazione():
    query = "SELECT id_stato_conservazione, descrizione FROM stato_conservazione"

    res = execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_status_serie():
    query = "SELECT id_status_serie, descrizione FROM status_serie"

    res = execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_periodicita():
    query = "SELECT id_periodicita, descrizione FROM periodicita"

    res = execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp


def get_genere_serie():
    query = "SELECT id_genere_serie, descrizione FROM genere_serie"

    res = execute_query_lookup(query)

    if res["op"] == "ok":
        status = 200
    else:
        status = 500
    resp = Response(json.dumps(res), status=status, mimetype="application/json")

    return resp
