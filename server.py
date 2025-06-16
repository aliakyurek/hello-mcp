from task import TaskManager, Task
from fastmcp import FastMCP



# mcp = FastMCP(host="127.0.0.1", port=8000, sse_path="/sse")
# default values are already set in FastMCP, so you can just use:
mcp = FastMCP()
tm = TaskManager()

tm.add_task("Eat breakfast",is_completed=True)
tm.add_task("Go to work")
tm.add_task("Attend meetings")
tm.add_task("Read a book")
tm.add_task("Exercise")


@mcp.tool()
def list_tasks() -> list[Task]:
    """
    List all tasks in the system.
    """
    return tm.list_tasks()

@mcp.resource("config://version")
def get_version() -> str:
    """
    Get the version of the application.
    """
    return "1.0.0"

@mcp.resource("tasks://{task_id}")
def get_task(task_id: int) -> str:
    """
    Get a specific task by its ID.
    """
    for task in tm.list_tasks():
        if task.id == task_id:
            return task.name
    raise ValueError(f"Task with ID {task_id} not found.")

@mcp.tool()
def add_task(name: str) -> list[Task]:
    """
    Add a new task to the system.
    """
    tm.add_task(name)
    return tm.list_tasks()

@mcp.tool()
def complete_task(task_id: int) -> Task:
    """
    Mark a task as completed.
    """
    return tm.complete_task(task_id)

if __name__ == "__main__":
    mcp.run(transport="sse")