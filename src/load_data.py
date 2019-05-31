#!/usr/bin/env python3

import argparse
import MySQLdb

def main():
    parser = argparse.ArgumentParser(description='Load data from MySQL')
    parser.add_argument(
        'dbname',
        type='string',
        help='Database from which to load data')
    args = parser.parse_args(['dbname'])

    conn = dbconn(args)
    results = get_information_object(dbconn)

    vars(results)
    
def dbconn(args):

    if not args.dbname:
        raise ValueError('You must define a DB_NAME environment variable')

    return MySQLdb.connect(host='db',port='3306',user='root',passwd='',
        db=args.dbname)

def get_information_object(dbconn):
    c=dbconn.cursor()
    c.execute("""SELECT * FROM information_object LIMIT 1""")
    
    return c.fetchone()

if __name__ == '__main__':
    main()