from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int = Field(..., description="The ID of the task")
    name: str = Field(..., description="The name of the task")
    is_completed: bool = Field(default=False, description="Whether the task is completed")


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, name: str, is_completed: bool=False) -> Task:
        task = Task(id=self.next_id, name=name, is_completed=is_completed)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        return self.tasks
    
    def remove_task(self, task_id: int) -> Task:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                return self.tasks.pop(i)
        raise ValueError(f"Task with ID {task_id} not found.")  

    def complete_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                task.is_completed = True
                return task
        raise ValueError(f"Task with ID {task_id} not found.")
