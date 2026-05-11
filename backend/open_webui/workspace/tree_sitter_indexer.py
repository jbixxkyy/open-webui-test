from pathlib import Path
from typing import Dict, List


class TreeSitterIndexer:
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)

    def index(self) -> List[Dict]:
        indexed = []

        for path in self.workspace_root.rglob('*.*'):
            if not path.is_file():
                continue

            indexed.append(
                {
                    'path': str(path.relative_to(self.workspace_root)),
                    'language': path.suffix.replace('.', ''),
                    'status': 'indexed',
                }
            )

        return indexed
