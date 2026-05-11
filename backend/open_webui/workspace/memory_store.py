from typing import Dict, List


class WorkspaceMemoryStore:
    def __init__(self):
        self.memory: Dict[str, List[str]] = {}

    def add_memory(self, scope: str, value: str):
        if scope not in self.memory:
            self.memory[scope] = []

        self.memory[scope].append(value)

    def get_memory(self, scope: str):
        return self.memory.get(scope, [])

    def clear_scope(self, scope: str):
        if scope in self.memory:
            del self.memory[scope]
