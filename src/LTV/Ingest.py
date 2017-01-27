import sqlite3
import logging
import ast
import os
conn = sqlite3.connect('events_user.db')
#c = conn.cursor() # connect database


def ingest(e,c):
        c = conn.cursor() # connect database
        for e in data:
                value_list = ()
                if e['type'] =='CUSTOMER':
                        for key in e.keys():
                                value_list = value_list + (e[key],)
                        c.execute("INSERT INTO CUSTOMER VALUES (?,?,?,?,?,?,?)", value_list)
                        # Save (commit) the changes
                        conn.commit()
                        # We can also close the connection if we are done with it.
                        # Just be sure any changes have been committed or they will be lost.

                elif e['type'] == 'ORDER':
                        for key in e.keys():
                                value_list = value_list + (e[key],)
                        c.execute("INSERT INTO ORDERTABLE VALUES (?,?,?,?,?,?)", value_list)
                        # Save (commit) the changes
                        conn.commit()

                elif e['type'] == 'IMAGE':
                        for key in e.keys():
                                value_list = value_list + (e[key],)
                        c.execute("INSERT INTO IMAGE VALUES (?,?,?,?,?,?,?)", value_list)
                        # Save (commit) the changes
                        conn.commit()
                elif e['type'] == 'VISIT':
                        for key in e.keys():
                                value_list = value_list + (e[key],)
                        c.execute("INSERT INTO VISIT VALUES (?,?,?,?,?,?)", value_list)
                        # Save (commit) the changes
                        conn.commit()
                else:
                        logging.info("unknown customer event type")


if __name__ == "__main__":
        c = conn.cursor() # connect database

        cwd = os.getcwd().split('/')
        data_path_relative = '/'.join(cwd[:-2])

        data_path = os.path.join(data_path_relative, 'input/input.txt')

        file = open(data_path, "r").read()
        data = ast.literal_eval(file)
        ingest(data,c)
        for row in c.execute('SELECT * FROM ORDERTABLE'):
                print row
        conn.close()
