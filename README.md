#Shutterfly Customer Lifetime Value 

By Stephanie Cheng

Design:

(1). Use the python sqlite3 to build the warehouse, it includes four tables, which are "CUSTOMER", "VISIT", "IMAGE", "ORDERTABLE"

(2). Use the Ingest.py to update the table, it will detect four type events, and put the values into each table, also ignore the unknown events for simplify

(3). Use the TopXSimpleLTV.py to get the top X LTV. You can change the top number (x) in main function 



how to test my code:

1. paste input and events you want to test to input.txt, like the sample events. (i.e, I have put same order evens to test my code)

2. Then run the Ingest function, it will put the events you put to the warehouse. (In order to test, I print all the order events)

3. Define the top x value (default =5), the run the TopXSimpleLTV.py, the top x value will be save to output/output.txt automatically.


If you have any questions, please contact me: zhangchengjob2015@gmail.com
