from datetime import timedelta, datetime

import dateutil.relativedelta as relativedelta
import dateutil.rrule as dr
import pytz
from flight_duration import airports, Flight


class FlightGenerator:
    """
    Generate a flight schedule
    - Third Monday of every month
    - Every 3 hours on certain day
    """

    def __init__(self, flight_id, origin, destination, duration):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def generate_flights(self, rule):
        flights = []
        for dt in rule:
            flights.append(Flight(
                flight_id=self.flight_id,
                origin=self.origin,
                destination=self.destination,
                departure=dt,
                arrival=self.calculate_arrival_time(dt)
            ))
        return flights

    def calculate_arrival_time(self, dep):
        origin_tz = pytz.timezone(self.origin.tz)
        dep_localized = origin_tz.localize(dep, is_dst=None)
        arr_localized = dep_localized + self.duration
        dest_tz = pytz.timezone(self.destination.tz)
        arr_asdest = dest_tz.normalize(arr_localized.astimezone(dest_tz))  # DST normalize
        return datetime.combine(arr_asdest.date(), arr_asdest.time())


generator = FlightGenerator(flight_id='AA123',
                            origin=airports['ATL'],
                            destination=airports['SVO'],
                            duration=timedelta(hours=13, minutes=25))

# third Monday of every month in 2018
flights = generator.generate_flights(dr.rrule(
    freq=dr.WEEKLY,
    byweekday=relativedelta.MO(3),
    dtstart=datetime(2018, 1, 1, 10, 30, 0),
    count=12
))

flights += generator.generate_flights(dr.rrule(
    freq=dr.HOURLY,
    interval=3,
    dtstart=datetime(2019, 1, 1, 15, 0, 0),
    count=3
))

flights += generator.generate_flights(dr.rrule(
    freq=dr.HOURLY,
    byhour=[10, 13],
    dtstart=datetime(2019, 2, 1, 15, 0, 0),
    until=datetime(2019, 2, 4, 15, 0, 0)
))

if __name__ == '__main__':
    for f in flights:
        print(f)
