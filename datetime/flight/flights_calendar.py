import calendar
import flight_duration


class FlightsCalendar(calendar.TextCalendar):
    """Custom Calendar with decorating flight days"""

    def __init__(self, firstweekday, flights):
        super(FlightsCalendar, self).__init__(firstweekday)
        self.dates_with_flight = set()
        for f in flights:
            self.dates_with_flight.add(f.departure.date())

    def is_flight_date(self, date):
        return date in self.dates_with_flight

    def days_with_flights(self, theyear, themonth):
        days = set()
        for date in self.itermonthdates(theyear, themonth):
            if self.is_flight_date(date):
                days.add(date.day)
        return days

    def split_into_weeks(self, monthdays):
        step = 7
        for i in range(0, len(monthdays), step):
            yield monthdays[i:i + step]

    def formatmonth(self, theyear, themonth, withyear=True, **kwargs):
        width = 4
        days_with_flights = self.days_with_flights(theyear, themonth)
        s = self.formatweekheader(width) + '\n'
        monthdays = list(self.itermonthdays2(theyear, themonth))
        for week in self.split_into_weeks(monthdays):
            s += self.formatweek(week, width, days_with_flights) + '\n'
        return s

    def formatweek(self, theweek, width, days_with_flights=set()):
        return ' '.join(
            self.formatday(day, wkday, width, day in days_with_flights) for (day, wkday) in theweek)

    def formatday(self, day, weekday, width, has_flight=True):
        s = super(FlightsCalendar, self).formatday(day, weekday, width).strip()
        if has_flight and day != 0:  # day = 0 : 範囲外
            s = '[' + s + ']'
        return s.center(width)


if __name__ == '__main__':
    c = FlightsCalendar(calendar.MONDAY, flight_duration.flights)
    s = c.formatmonth(2018, 3, )

    print(s)
