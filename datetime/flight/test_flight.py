import unittest
from datetime import datetime, timedelta
from unittest.mock import *

from flight_duration import Flight, airports
from pytz import timezone


class TestFlight(unittest.TestCase):
    def setUp(self):
        self.flights = [
            Flight(flight_id='AA123',
                   origin=airports['ATL'],
                   destination=airports['SVO'],
                   departure=datetime(2018, 1, 1, 10, 10, 0),
                   arrival=datetime(2018, 1, 2, 7, 12, 0))]

    def test_time_to_departure(self):
        with patch('flight_duration.datetime') as mock_datetime, \
                patch('flight_duration.get_localzone') as mock_get_localzone:
            mock_datetime.now.return_value = datetime(2018, 1, 1, 10, 10, 0)
            mock_get_localzone.return_value = timezone('US/Eastern')

            self.assertEqual(self.flights[0].time_to_departure(),
                             timedelta(hours=0))

            mock_get_localzone.return_value = timezone('US/Pacific')
            self.assertEqual(self.flights[0].time_to_departure(),
                             timedelta(hours=-3))
