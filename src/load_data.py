#!/usr/bin/env python3

import argparse
import MySQLdb

parser = argparse.ArgumentParser(description='Load data from MySQL')
parser.add_argument(
    '--db', "-d",
    help='Database from which to load data')


def main():
    conn = dbconn()
    # results = get_information_object(conn)


def get_db_config(*args):
    config = {}

    # Get command line arguments
    if args:
        pargs = parser.parse_args(args)
    else:
        pargs = parser.parse_args()

    if pargs.db:
        config['dbname'] = pargs.db

    return config


def dbconn():
    config = get_db_config()

    if 'dbname' not in config:
        raise ValueError('You must define a database name')

    # return MySQLdb.connect(host='db', port='3306', user='root', passwd='', db=config['dbname'])


def get_information_object(dbconn):
    c = dbconn.cursor()
    c.execute("""SELECT * FROM information_object LIMIT 1""")

    return c.fetchone()


if __name__ == '__main__':
    main()
