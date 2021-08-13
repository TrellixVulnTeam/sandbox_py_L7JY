import textwrap
from datetime import datetime, timedelta

import pytz
from airport import load_airports
from tzlocal import get_localzone


class Flight:
    def __init__(self, flight_id, origin, destination, departure, arrival):
        self.id = flight_id
        self.origin = origin
        self.destination = destination

        self.departure = self.localize_flight_datetime(departure, origin.tz)
        self.arrival = self.localize_flight_datetime(arrival, destination.tz)

    @staticmethod
    def localize_flight_datetime(date_time, tz_name):
        # return pytz.timezone(tz_name).localize(date_time, is_dst=None)  # default: is_dst=False
        tz = pytz.timezone(tz_name)
        try:
            return tz.localize(date_time, is_dst=None)
        except pytz.exceptions.AmbiguousTimeError:
            return tz.localize(date_time, is_dst=True)

    @property
    def check_in(self):
        # return self.departure - timedelta(hours=3)  # check-in time offset changed
        return self.departure.tzinfo.normalize(self.departure - timedelta(hours=3))

    @property
    def duration(self):
        return self.arrival - self.departure

    def time_to_departure(self):
        # return self.departure - datetime.now()  # NG: aware - naive
        return self.departure - get_localzone().localize(datetime.now())

    def __str__(self):
        return textwrap.dedent('''\
        Flight {0.id}:
            from        : {0.origin}
            to          : {0.destination}
            departure   : {0.departure} {0.departure.tzinfo}
            arrival     : {0.arrival} {0.arrival.tzinfo}
            duration    : {0.duration}

            time to departure       : {ttd}
            check-in                : {0.check_in}
        '''.format(self, ttd=self.time_to_departure()))


airports = load_airports('../../data/airports.csv')

flights = [
    Flight(flight_id='AA123',
           origin=airports['ATL'],
           destination=airports['SVO'],
           departure=datetime(2018, 1, 1, 10, 10, 0),
           arrival=datetime(2018, 1, 2, 7, 12, 0)),
    Flight(flight_id='DST01',
           origin=airports['BRU'],
           destination=airports['ATL'],
           departure=datetime(2018, 3, 25, 1, 10, 0),
           arrival=datetime(2018, 3, 25, 7, 0, 0)),
    Flight(flight_id='DST02',
           origin=airports['BRU'],
           destination=airports['ATL'],
           # departure=datetime(2018, 3, 25, 2, 10, 0),  # NonExistentTimeError (winter -> summer)
           # departure=datetime(2018, 10, 28, 2, 10, 0),  # AmbiguousTimeError (summer -> winter)
           departure=datetime(2018, 3, 25, 3, 10, 0),
           arrival=datetime(2018, 3, 25, 7, 0, 0))
]

if __name__ == '__main__':
    for f in flights:
        print(f)
