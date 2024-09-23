#
# datatier.py
#
# Executes SQL queries against the given database.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#
import sqlite3


########################################################
#
# select_one_row:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# the first row retrieved by the query. The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: first row retrieved by the given query;
#          if an error occurs a msg is output and None
#          is returned.
#
def select_one_row(dbConn, sql, parameters = None):
    if (parameters == None):
       parameters = []

    dbCursor = dbConn.cursor()

    try:
       dbCursor.execute(sql, parameters)
       row = dbCursor.fetchone()
       return row;
    except Exception as err:
       print("select_one_row failed:", err)
       return None
    finally:
       dbCursor.close()


########################################################
#
# select_n_rows:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# a list of rows retrieved by the query. The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: a list of 0 or more rows retrieved by the 
#          given query; if an error occurs a msg is 
#          output and None is returned.
#
def select_n_rows(dbConn, sql, parameters = None):
    if (parameters == None):
       parameters = []

    dbCursor = dbConn.cursor()

    try:
       dbCursor.execute(sql, parameters)
       rows = dbCursor.fetchall()
       return rows;
    except Exception as err:
       print("select_n_rows failed:", err)
       return None
    finally:
       dbCursor.close()
