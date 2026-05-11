import subprocess
from typing import List


class RipgrepSearch:
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def search(self, query: str) -> List[str]:
        try:
            process = subprocess.run(
                ['rg', query, self.workspace_root],
                capture_output=True,
                text=True,
            )

            return process.stdout.splitlines()

        except Exception:
            return []
