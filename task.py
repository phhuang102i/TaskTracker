
import json, os
from collections import defaultdict
from datetime import datetime
from functools import partial

JSON_FILE_NAME = "./db.json"

tasks_in_memory = defaultdict(dict)


class Task:
    def __init__(self, id=None, description=None, status=None, created_at=None, updated_at=None):
        # auto incr here
        self.id = id
        self.description = description
        self.status = status
        self.created_at = None
        self.updated_at = None
    

    @staticmethod
    def get_tasks_from_file() -> defaultdict:
        global tasks_in_memory

        if tasks_in_memory:
            return tasks_in_memory

        if not os.path.exists(JSON_FILE_NAME):
            with open(JSON_FILE_NAME, "w") as f:
                json.dump({}, f, indent=4)
        with open(JSON_FILE_NAME, "r") as f:
            tasks = json.load(f)
            tasks_in_memory = defaultdict(dict, tasks)

        return tasks_in_memory
    
    @staticmethod
    def save_task_to_file():
        with open(JSON_FILE_NAME, "w") as f:
            json.dump(tasks_in_memory, f, indent=4)
    
    @staticmethod
    def get(task_id):
        task_objs = Task.get_tasks_from_file()
        if task_id not in task_objs:
            raise ValueError(f"Input id {task_id} does not exists")

        return Task(
            id=task_id,
            description=task_objs[task_id]["description"],
            status=task_objs[task_id]["status"],
            created_at=task_objs[task_id]["createdAt"],
            updated_at=task_objs[task_id]["updatedAt"],
        )


    def save(self):
        global tasks_in_memory
        task_objs = Task.get_tasks_from_file()
        if not self.id:
            self.id = str(max([*(int(k) for k in task_objs.keys()), 0]) + 1)

        task_objs[self.id].update(
            {
                "description": self.description,
                "status": self.status,
                "createdAt": datetime.isoformat(datetime.now()) if self.created_at is None else self.created_at,
                "updatedAt": datetime.isoformat(datetime.now())
            }
        )
        Task.save_task_to_file()


def delete_task(task_id: int, *args) -> None:
    global tasks_in_memory
    task = Task.get(task_id)
    tasks_in_memory.pop(task.id)
    Task.save_task_to_file()

def add_task(task_name: str, *args) -> None:
    new_task = Task(
        description=task_name,
        status="todo"
    )
    new_task.save()
    print(f"Task added successfully (ID: {new_task.id})")
    
def update_task(task_id, description=None, status=None) -> None:
    task = Task.get(task_id)
    if description is not None:
        task.description = description
    if status is not None:
        task.status = status
    task.save()

def mark_task_in_progress(task_id) -> None:
    update_task(task_id, status="in-progress")

def mark_task_complete(task_id) -> None:
    update_task(task_id, status="done")


def list_task(status=None) -> None:
    task_objs = Task.get_tasks_from_file()

    for task_id, task_attr in task_objs.items():

        if status is not None and task_attr["status"] != status:
            continue
        print({
            task_id: task_attr
        })
        
