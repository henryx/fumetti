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


def get_valuta():
    try:
        data = []
        db = utils.database.get_db()

        with closing(db.cursor()) as cur:
            cur.execute("SELECT id_valuta, simbolo FROM valuta")
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    except psycopg2.OperationalError:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp


def get_rilegatura():
    try:
        data = []
        db = utils.database.get_db()

        with closing(db.cursor()) as cur:
            cur.execute("SELECT id_rilegatura, descrizione FROM rilegatura")
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    except psycopg2.OperationalError:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp


def get_conservazione():
    try:
        data = []
        db = utils.database.get_db()

        with closing(db.cursor()) as cur:
            cur.execute("SELECT id_stato_conservazione, descrizione FROM stato_conservazione")
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    except psycopg2.OperationalError:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp


def get_status_serie():
    try:
        data = []
        db = utils.database.get_db()

        with closing(db.cursor()) as cur:
            cur.execute("SELECT id_status_serie, descrizione FROM status_serie")
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    except psycopg2.OperationalError:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp


def get_periodicita():
    try:
        data = []
        db = utils.database.get_db()

        with closing(db.cursor()) as cur:
            cur.execute("SELECT id_periodicita, descrizione FROM periodicita")
            results = cur.fetchall()
            for item in results:
                data.append({"id": item[0], "name": item[1]})

        res = {"data": data, "op": "ok"}
        resp = Response(json.dumps(res), status=200, mimetype="application/json")
    except psycopg2.OperationalError:
        res = {"op": "ko", "msg": "Error to connect to database"}
        resp = Response(json.dumps(res), status=500, mimetype="application/json")

    return resp
