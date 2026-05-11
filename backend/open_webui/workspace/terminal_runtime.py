import subprocess
from typing import Dict


class TerminalRuntime:
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def run_command(self, command: str) -> Dict:
        try:
            process = subprocess.run(
                command,
                shell=True,
                cwd=self.workspace_root,
                capture_output=True,
                text=True,
            )

            return {
                'success': process.returncode == 0,
                'stdout': process.stdout,
                'stderr': process.stderr,
                'returncode': process.returncode,
            }

        except Exception as error:
            return {
                'success': False,
                'stdout': '',
                'stderr': str(error),
                'returncode': -1,
            }
