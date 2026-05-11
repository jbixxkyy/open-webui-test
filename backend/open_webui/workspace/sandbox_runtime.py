import subprocess
from typing import Dict


class SandboxRuntime:
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def execute(self, command: str) -> Dict:
        process = subprocess.run(
            command,
            shell=True,
            cwd=self.workspace_root,
            capture_output=True,
            text=True,
            timeout=30,
        )

        return {
            'stdout': process.stdout,
            'stderr': process.stderr,
            'returncode': process.returncode,
        }
