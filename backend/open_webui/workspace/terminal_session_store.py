from typing import Dict


class TerminalSessionStore:
    def __init__(self):
        self.sessions: Dict[str, Dict] = {}

    def create(self, session_id: str, payload: Dict):
        self.sessions[session_id] = payload
        return payload

    def get(self, session_id: str):
        return self.sessions.get(session_id)

    def list(self):
        return list(self.sessions.values())

    def remove(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]
