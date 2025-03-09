import heapq

def priority_task_scheduler(tasks):
    heap = []
    
    for task, priority in tasks:
        heapq.heappush(heap, (priority, task))  # Push tasks with priority
    
    while heap:
        priority, task = heapq.heappop(heap)
        print(f"Processing task: {task} with priority {priority}")

tasks = [('task1', 2), ('task2', 1), ('task3', 3)]
priority_task_scheduler(tasks)
