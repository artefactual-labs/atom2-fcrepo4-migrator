import pytest

@pytest.fixture
def dbconn():
    import MySQLdb, os

    dbhost = os.environ.get('DB_HOST', 'localhost')
    dbport = os.environ.get('DB_PORT', '3306')
    dbuser = os.environ.get('DB_USER', None)
    dbpass = os.environ.get('DB_PASS', '')
    dbname = os.environ.get('DB_NAME', None)    

    if not dbname:
        raise ValueError('You must define a DB_NAME environment variable')

    return MySQLdb.connect(host=dbhost,port=dbport,user=dbuser,passwd=dbpass,
        db=dbname)

def test_get_information_object(dbconn):
    c=dbconn.cursor()
    c.execute("""SELECT * FROM information_object LIMIT 1""")
    assert c.fetchone() is not None
