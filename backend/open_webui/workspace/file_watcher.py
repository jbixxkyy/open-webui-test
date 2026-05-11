from pathlib import Path
from typing import Dict, List


class WorkspaceFileWatcher:
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)
        self.snapshot: Dict[str, float] = {}

    def scan(self) -> List[str]:
        changed = []

        for path in self.workspace_root.rglob('*'):
            if not path.is_file():
                continue

            relative = str(path.relative_to(self.workspace_root))
            modified = path.stat().st_mtime

            previous = self.snapshot.get(relative)

            if previous is None or previous != modified:
                changed.append(relative)

            self.snapshot[relative] = modified

        return changed
