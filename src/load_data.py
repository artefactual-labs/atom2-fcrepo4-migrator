#!/usr/bin/env python3

import argparse
import MySQLdb


def main():
    args = parse_args()

    if not args['db']:
        raise ValueError('You must define a DB_NAME environment variable')

    conn = dbconn(args)
    results = get_information_object(conn)

    vars(results)


def parse_args(vargs):
    parser = argparse.ArgumentParser(description='Load data from MySQL')
    parser.add_argument(
        '--db', "-d",
        type='string',
        help='Database from which to load data')

    if vargs:
        return parser.parse_args(vargs)
    else:
        return parser.parse_args()


def dbconn(args):

    if not args.dbname:
        raise ValueError('You must define a DB_NAME environment variable')

    return MySQLdb.connect(host='db', port='3306', user='root', passwd='',
                           db=args.dbname)


def get_information_object(dbconn):
    c = dbconn.cursor()
    c.execute("""SELECT * FROM information_object LIMIT 1""")

    return c.fetchone()


if __name__ == '__main__':
    main()
