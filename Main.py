from Task import Task
from Compute import Compute

if __name__ == '__main__':
    task1 = Task(name='t1', phase=0, ex_time=1, period=4, deadline=4)
    task2 = Task(name='t2', phase=0, ex_time=2, period=5, deadline=7)
    task3 = Task(name='t3', phase=0, ex_time=5, period=20, deadline=20)

    tasks_array = [task1, task2, task3]

    compute = Compute(H=20, F=4, tasks=tasks_array)
    jobs = compute.get_jobs()
    print jobs
