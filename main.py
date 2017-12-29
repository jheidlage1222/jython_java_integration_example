'''
Created on Dec 20, 2017

@author: jjh39
'''
import sys

from com.ziclix.python.sql import zxJDBC
import py_to_java_test as p
import py_to_java_httpclient as pClient
################################################################################

#DATABASE    = "solarsys.db"
#JDBC_URL    = "jdbc:sqlite:%s"  % DATABASE
JDBC_URL = "jdbc:sqlite:D:/eclipse_workspace/Sandbox/misc/AppConfig.db"
JDBC_DRIVER = "org.sqlite.JDBC"

MY_QUERY = "SELECT * FROM Application"
#TABLE_NAME      = "planet"
#TABLE_DROPPER   = "drop table if exists %s;"                      % TABLE_NAME
#TABLE_CREATOR   = "create table %s (name, size, solar_distance);" % TABLE_NAME
#RECORD_INSERTER = "insert into %s values (?, ?, ?);"              % TABLE_NAME


################################################################################

def main():
    p.RunClientTest()
    #pClient.RunClientProxyTest()
    return
    msg = ""
    print("Starting run.....")
    dbConn = getConnection(JDBC_URL, JDBC_DRIVER)
    cursor = dbConn.cursor()
    try:
        cursor.execute(MY_QUERY)
        for row in cursor.fetchall():
            print("meh")
    except zxJDBC.DatabaseError, msg:
        print( msg)
        sys.exit(1)

#     try:
#         cursor.executemany(RECORD_INSERTER, PLANET_DATA)
#         dbConn.commit()
#     except zxJDBC.DatabaseError, msg:
#         print msg
#         sys.exit(2)
# 
#     try:
#         cursor.execute(PLANET_QUERY)
#         for row in cursor.fetchall():
#             name, size, dist = row[:]
#             print "%-16.16s  %-8.8s  %4d" % (name, size, dist)
#     except zxJDBC.DatabaseError, msg:
#         print msg
#         sys.exit(3)
    print("Program terminated")
    cursor.close()
    dbConn.close()
    sys.exit(0)

################################################################################

def getConnection(jdbc_url, driverName):
    msg = ""
    """
        Given the name of a JDBC driver class and the url to be used 
        to connect to a database, attempt to obtain a connection to 
        the database.
    """

    try:
        # no user/password combo needed here, hence the None, None
        
        dbConn = zxJDBC.connect(jdbc_url, None, None, driverName)
    except zxJDBC.DatabaseError, msg:
        print(msg)
        sys.exit(-1)

    return dbConn

################################################################################

if __name__ == '__main__':
    main()
