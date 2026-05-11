from dataclasses import dataclass
from typing import List


@dataclass
class AgentTask:
    id: str
    title: str
    status: str


class AgentManager:
    def __init__(self):
        self.tasks: List[AgentTask] = []

    def create_task(self, task_id: str, title: str):
        task = AgentTask(
            id=task_id,
            title=title,
            status='pending'
        )

        self.tasks.append(task)
        return task

    def update_status(self, task_id: str, status: str):
        for task in self.tasks:
            if task.id == task_id:
                task.status = status
                return task

        return None

    def get_tasks(self):
        return self.tasks
