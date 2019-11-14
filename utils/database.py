# -*- coding: utf-8 -*-

# Copyright (C) 2019 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project Name: fumetti
# Description   A RESTful API for managing a collection of comic books
# License       GPL version 2 (see LICENSE for details)
from contextlib import closing

import psycopg2.pool
from flask import g, current_app


def open_db(host, port, dbname, user, password):
    pool = psycopg2.pool.ThreadedConnectionPool(1, 20,
                                                host=host, port=port,
                                                dbname=dbname, user=user,
                                                password=password)

    return pool


def get_db():
    if "db" not in g:
        g.db = current_app.config["pgpool"].getconn()

    return g.db


def close_db():
    db = g.pop('db', None)

    if db:
        current_app.config["pgpool"].putconn(db)


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
