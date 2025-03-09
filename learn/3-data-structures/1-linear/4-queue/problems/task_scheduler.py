import time
import threading

def worker(task_list):
    while task_list:
        task = task_list.pop(0)
        print(f"Processing task: {task}")
        time.sleep(1)

def task_scheduler(tasks):
    threads = []
    
    # Start worker threads
    for _ in range(2):
        thread = threading.Thread(target=worker, args=(tasks,))
        thread.start()
        threads.append(thread)
    
    # Wait for workers to finish
    for thread in threads:
        thread.join()

tasks = ['task1', 'task2', 'task3', 'task4']
task_scheduler(tasks)
