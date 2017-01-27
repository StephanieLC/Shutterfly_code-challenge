import sqlite3


if __name__ == "__main__":
    conn = sqlite3.connect('events_user.db')
    c = conn.cursor() # connect database
    # ['last_name', 'event_time', 'verb', 'key', 'adr_state', 'adr_city', 'type']
    # ['event_time', 'tags', 'verb', 'key', 'customer_id', 'type']
    # ['camera_make', 'event_time', 'camera_model', 'verb', 'key', 'customer_id', 'type']
    # ['total_amount', 'event_time', 'verb', 'key', 'customer_id', 'type']
    c.execute('''CREATE TABLE CUSTOMER
                 (last_name text, event_time text, verb text, key text, adr_state text,adr_city text,type text)''') # create table

    c.execute('''CREATE TABLE VISIT
                 (event_time text, tags text, verb text, key text, customer_id text,type text)''') # create table

    c.execute('''CREATE TABLE IMAGE
                 (camera_make text, event_time text, camera_model text, verb text, key text,customer_id text,type text)''') # create table

    c.execute('''CREATE TABLE ORDERTABLE
                 (total_amount text, event_time text, verb text, key text, customer_id text, type text)''') # create table
    conn.commit()  # save table
    conn.close()
