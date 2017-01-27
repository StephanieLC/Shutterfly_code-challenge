import sqlite3
import logging
import ast
import os
conn = sqlite3.connect('events_user.db')

def TopXSimpleLTVCustomers(x,c):
    c.execute("create temporary table temp1 as select sum(total_amount) as total_amount,customer_id from ORDERTABLE group by customer_id")
    # Save (commit) the changes
    conn.commit()
    c.execute("create temporary table temp2 as select max(event_time) as max_event_time,customer_id from ORDERTABLE group by customer_id")
    # Save (commit) the changes
    conn.commit()
    c.execute("create temporary table temp3 as select min(event_time) as min_event_time,customer_id from ORDERTABLE group by customer_id")
    # Save (commit) the changes
    conn.commit()
    c.execute("create temporary table result as select distinct temp1.total_amount/(((temp2.max_event_time-temp3.min_event_time)/7)+1) as ACV,temp1.customer_id from temp1 left join temp2 on temp1.customer_id=temp2.customer_id left join temp3 on temp1.customer_id=temp3.customer_id")
    # Save (commit) the changes
    conn.commit()
    result=c.execute("SELECT * FROM result order by ACV desc limit %s" % x)
    conn.commit()
    return result


if __name__ == "__main__":
    cwd = os.getcwd().split('/')
    data_path_relative = '/'.join(cwd[:-2])
    # execute the topx query, i.e: x = 2
    c = conn.cursor()
    x = 5
    result=TopXSimpleLTVCustomers(x, c)

    # save the results to output.txt
    output_txt_path = os.path.join(data_path_relative, 'output/output.txt')
    thefile = open(output_txt_path, 'w')

    for item in result:
        print >> thefile, item

    conn.close()
