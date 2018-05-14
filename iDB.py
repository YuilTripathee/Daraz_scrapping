import json
import pymysql
if __name__ == '__main__':
    # extract database server configuration
    with open('database/DBconf.json') as fp:
        dbConf = json.load(fp)
        fp.close()

    # start a connection
    db = pymysql.connect(dbConf['server'], dbConf['username'], dbConf['password'], dbConf['database'])
    # make a cursor to work on database (to execute queries)
    cursor = db.cursor()
    print('Connection established with database.')
    
    # work on queries
    while True:
        command = input('> ')
        try:
            cursor.execute(command)
            db.commit()
        except:
            print('Error')
            db.rollback()