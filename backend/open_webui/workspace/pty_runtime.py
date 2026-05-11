import os
import pty
import subprocess
from typing import Dict


class PTYRuntime:
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def create_session(self, command: str = '/bin/bash') -> Dict:
        master, slave = pty.openpty()

        process = subprocess.Popen(
            command,
            shell=True,
            cwd=self.workspace_root,
            stdin=slave,
            stdout=slave,
            stderr=slave,
            close_fds=True,
        )

        return {
            'pid': process.pid,
            'master_fd': master,
            'slave_fd': slave,
        }

    def read_output(self, master_fd: int, size: int = 4096):
        return os.read(master_fd, size).decode(errors='ignore')
