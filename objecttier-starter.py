#
# objecttier
#
# Builds objects from data retrieved through the data tier.
#
# Original author: Prof. Joe Hummel
#
import datatier
#
# do not import other modules
#

########################################################
#
# Station:
#
# Constructor(...)
# Properties:
#   Station_ID: int
#   Station_Name: string
#   Ridership: int
#   Percent_Ridership: float
#
class Station:
   pass


########################################################
#
# Stop:
#
# Constructor(...)
# Properties:
#   Stop_ID: int
#   Stop_Name: string
#   Direction: string
#   Accessible: boolean (True/False)
#   Latitude: float
#   Longitude: float
#   Lines: list of strings
#
class Stop:
   pass


########################################################
#
# get_stations:
#
# gets and returns all stations whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of stations in ascending order by name;
#          returns None if an error occurs.
#
def get_stations(dbConn, pattern):
   pass


########################################################
#
# get_stops:
#
# gets and returns all stops at a given station; the 
# given station name must match exactly (no wildcards).
# If there is no match, an empty list is returned.
#
# Returns: a list of stops in ascending order by name,
#          then in ascending order by id if two stops
#          have the same name; returns None if an error
#          occurs.
#
def get_stops(dbConn, name):
   pass
