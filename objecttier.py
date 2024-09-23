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
    def __init__(self, Station_ID: int, Station_Name: str, Ridership: int, Percent_Ridership: float) -> None:
        self.__Station_ID = Station_ID
        self.__Station_Name = Station_Name
        self.__Ridership = Ridership
        self.__Percent_Ridership = Percent_Ridership

    @property
    def Station_ID(self) -> int:
        return self.__Station_ID

    @property
    def Station_Name(self) -> str:
        return self.__Station_Name

    @property
    def Ridership(self) -> int:
        return self.__Ridership

    @property
    def Percent_Ridership(self) -> float:
        return self.__Percent_Ridership


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
    def __init__(self, Stop_ID: int, Stop_Name: str, Direction: str, Accessible: bool, Latitude: float, Longitude: float, Lines: list[str]) -> None:
        self.__Stop_ID = Stop_ID
        self.__Stop_Name = Stop_Name
        self.__Direction = Direction
        self.__Accessible = Accessible
        self.__Latitude = Latitude
        self.__Longitude = Longitude
        self.__Lines = Lines

    @property
    def Stop_ID(self) -> int:
        return self.__Stop_ID

    @property
    def Stop_Name(self) -> str:
        return self.__Stop_Name

    @property
    def Direction(self) -> str:
        return self.__Direction

    @property
    def Accessible(self) -> bool:
        return self.__Accessible

    @property
    def Latitude(self) -> float:
        return self.__Latitude

    @property
    def Longitude(self) -> float:
        return self.__Longitude

    @property
    def Lines(self) -> list[str]:
        return self.__Lines

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
    entries = datatier.select_n_rows(dbConn, f"""
        SELECT Station_Name, Stations.Station_ID, SUM(Num_Riders) FROM Stations
        JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID
        WHERE Station_Name LIKE "{pattern}"
        GROUP BY Stations.Station_ID
        ORDER BY Station_Name
    """)

    if not entries:
        return None

    total, = datatier.select_one_row(dbConn, """
        SELECT SUM(Num_Riders) FROM Ridership
    """)

    results = []
    for Station_Name, Station_ID, Num_Riders in entries:
        results.append(Station(Station_Name, Station_ID, Num_Riders, 100*Num_Riders/total))

    return results


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
    station = datatier.select_one_row(dbConn, """
        SELECT Station_ID FROM Stations
        WHERE Station_Name = ?
    """, [name])

    if not station:
        return []

    station_id, = station

    stops = datatier.select_n_rows(dbConn, """
        SELECT Stop_ID, Stop_Name, Direction, ADA, Latitude, Longitude
        FROM Stops
        WHERE Station_ID = ?
        ORDER BY Stop_Name, Stop_ID
    """, [station_id])

    results = []
    for Stop_ID, Stop_Name, Direction, ADA, Latitude, Longitude in stops:
        # get lines
        lines = datatier.select_n_rows(dbConn, """
            SELECT Color FROM Lines
            JOIN StopDetails ON Lines.Line_ID = StopDetails.Line_ID
            JOIN Stops ON StopDetails.Stop_ID = Stops.Stop_ID
            WHERE StopDetails.Stop_ID = ?
            ORDER BY Color
        """, [Stop_ID])

        results.append(Stop(Stop_ID, Stop_Name, Direction, ADA, Latitude, Longitude, [x for x, in lines]))

    return results
