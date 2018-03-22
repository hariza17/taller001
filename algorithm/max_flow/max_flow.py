from algorithm.periodic_scheduler import PeriodicScheduler


class MaxFlow(PeriodicScheduler):
    def __init__(self, H, F, tasks):
        PeriodicScheduler.__init__(self, H, F, tasks)


