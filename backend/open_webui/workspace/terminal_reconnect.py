from typing import Dict


class TerminalReconnectManager:
    def __init__(self):
        self.sessions: Dict[str, Dict] = {}

    def register(self, session_id: str, payload: Dict):
        self.sessions[session_id] = payload

    def reconnect(self, session_id: str):
        return self.sessions.get(session_id)
