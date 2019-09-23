"""
Using Context manager
pushing data
"""

from observers import AbsCtxObserver
from subjects import AbsCtxSubject


class CurrentKPIs(AbsCtxObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self, values):
        self.open_tickets, self.closed_tickets, self.new_tickets = values
        self.display()

    def display(self):
        print('Current open tickets: {}'.format(self.open_tickets))
        print('New tickets in last hour: {}'.format(self.closed_tickets))
        print('Tickets closed in last hour: {}'.format(self.new_tickets))
        print('*****\n')

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)


class ForecastKPIs(AbsCtxObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self, values):
        self.open_tickets, self.closed_tickets, self.new_tickets = values
        self.display()

    def display(self):
        print('Forecast open tickets: {}'.format(self.open_tickets))
        print('New tickets expected in next hour: {}'.format(self.closed_tickets))
        print('Tickets expected to be closed in next hour: {}'.format(self.new_tickets))
        print('*****\n')

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)


class KPIs(AbsCtxSubject):
    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self.notify(
            (open_tickets, closed_tickets, new_tickets)  # push data directly
        )


if __name__ == '__main__':
    # Report on current KPI values
    with KPIs() as kpis:
        with CurrentKPIs(kpis), ForecastKPIs(kpis):
            kpis.set_kpis(25, 10, 5)
            kpis.set_kpis(100, 50, 30)
            kpis.set_kpis(50, 10, 20)

    print('\n***Exited context managers.***\n\n')
    kpis.set_kpis(150, 110, 120)
