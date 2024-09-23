#
# Program to analyze data from CTA L daily ridership database.
# This is a simplified version of the program for Project 01,
# and works mainly with stations and stops; console-based only,
# all plotting has been removed.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#
# References: 
#  learning python: https://www.w3schools.com/python/
#  sqlite programming: https://docs.python.org/3/library/sqlite3.html
#
import sqlite3
import objecttier


##################################################################  
# 
# retrieve_stations
#
def retrieve_stations(dbConn):
    print()
    name = input("Enter partial station name (wildcards _ and %): ")

    stations = objecttier.get_stations(dbConn, name)

    if stations is None:  # error
        print("**Internal error: retrieve_stations")
    elif len(stations) == 0:
        print("**No stations found...")
    else:
        for s in stations:
            print(s.Station_ID, ":", 
                  s.Station_Name,
                  "[ridership:", 
                  f"{s.Ridership:,}", 
                  f"({s.Percent_Ridership:.2f}%)]")


##################################################################  
# 
# retrieve_stops
#
def retrieve_stops(dbConn):
    print()
    name = input("Enter station name (exact, no wildcards): ")

    stops = objecttier.get_stops(dbConn, name)

    if stops is None:  # error
        print("**Internal error: retrieve_stops")
    elif len(stops) == 0:
        print("**Station not found...")
    else:
        for s in stops:
           print(s.Stop_ID, ":", s.Stop_Name)

           if s.Accessible:
             print("  stop is accessible")
           else:
             print("  stop is not accessible")

           print("  Direction:", s.Direction)

           print("  Lines:", end=" ")
           for line in s.Lines:
              print(line, end=" ")
           print()

           print("  Location:", f"{s.Latitude, s.Longitude}")


##################################################################  
#
# main
#
print('** Welcome to the simplified CTA L analysis app **')

dbConn = sqlite3.connect('CTA2_L_daily_ridership.db')

print()
cmd = input("Please enter a command (1-9, x to exit): ")

while cmd != "x":
    if cmd == "1":
        retrieve_stations(dbConn)
    elif cmd == "2":
        retrieve_stops(dbConn)
    else:
        print("**Error, unknown command, try again...")

    print()
    cmd = input("Please enter a command (1-9, x to exit): ")

#
# done
#
