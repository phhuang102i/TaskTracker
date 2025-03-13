# TaskTracker
TaskTracker project from [roadmapsh](https://roadmap.sh/projects/task-tracker)


## Start
```
python main.py
```

## Add a task
```
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

## Update & Delete a task
```
# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
```

## Mark task in-progress or complete
```
# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1
```

## List task
```
# Listing all tasks
task-cli list
# List task by status
task-cli list todo

```

