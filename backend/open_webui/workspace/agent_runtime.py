from datetime import datetime
from typing import Dict, List


class AgentRuntime:
    def __init__(self):
        self.tasks: List[Dict] = []

    def start_task(self, task: Dict):
        runtime_task = {
            'id': len(self.tasks) + 1,
            'task': task,
            'status': 'running',
            'started_at': datetime.utcnow().isoformat(),
            'logs': ['Task started'],
            'retry_count': 0,
        }

        runtime_task['status'] = 'completed'
        runtime_task['logs'].append('Task completed')

        self.tasks.append(runtime_task)

        return runtime_task

    def get_tasks(self):
        return self.tasks
