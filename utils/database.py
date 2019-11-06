# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
from contextlib import closing

import psycopg2
from flask import g, current_app


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(host=current_app.config["DATABASE_HOST"],
                                port=current_app.config["DATABASE_PORT"],
                                dbname=current_app.config["DATABASE_NAME"],
                                user=current_app.config["DATABASE_USER"],
                                password=current_app.config["DATABASE_PASSWORD"])

    return g.db


def close_db():
    db = g.pop('db', None)

    if db:
        db.close()


def insert_albo(db, data):
    query = "INSERT INTO albi(id_serie, numero_albo, data_pubblicazione, prezzo_copertina, id_valuta, id_rilegatura, id_stato_conservazione, note) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

    with closing(db.cursor()) as cur:
        try:
            cur.execute(query, (data["serie"], data["numero"], data["date"], data["prezzo"], data["valuta"],
                                data["rilegatura"], data["conservazione"], data["note"]))
            db.commit()
        except psycopg2.Error as e:
            return False
        return True
