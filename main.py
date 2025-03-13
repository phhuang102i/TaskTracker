import shlex
from enum import StrEnum
from utils import EnumContainsMeta
from task import add_task, update_task, delete_task, mark_task_complete, mark_task_in_progress, list_task

class ValidAction(StrEnum, metaclass=EnumContainsMeta):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"
    MARK_IN_PROGRESS = "mark-in-progress"
    MARK_DONE = "mark-done"
    LIST = "list"

def parse_user_input(user_input: str) -> None:

    user_input_args = shlex.split(user_input)
    action = user_input_args[0]
    exit_cli = False

    match action:
        case ValidAction.ADD.value:
            add_task(*user_input_args[1:])
        case ValidAction.UPDATE.value:
            update_task(*user_input_args[1:])
        case ValidAction.DELETE.value:
            delete_task(*user_input_args[1:])
        case ValidAction.MARK_IN_PROGRESS.value:
            mark_task_in_progress(*user_input_args[1:])
        case ValidAction.MARK_DONE.value:
            mark_task_complete(*user_input_args[1:])
        case ValidAction.LIST.value:
            list_task(*user_input_args[1:])
        case "exit":
            exit_cli = True
        case _:
            raise Exception(f"Action {action} is invalid")
        
    return exit_cli


if __name__ == '__main__':
    
    while(True):
        user_input = input("task-cli ")
        try:
            exit_cli = parse_user_input(user_input)
        except ValueError as e:    
            print(e)
        else:
            if exit_cli is True: 
                break
        
