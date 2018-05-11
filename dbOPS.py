# import library necessary for Python to work with MySQL server
import PyMySQL

if __name__ == '__main__':
    # Open database connection
    db = PyMySQL.connect("localhost", "root", "123456", "TESTDB")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute a SQL query using execute() method
    cursor.execute("SELECT VERSION()")

    # fetch a single row using fetchone() method
    data = cursor.fetchone()

    print('Database version is %s' % data)

    # disconnect a server
    db.close()