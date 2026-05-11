from collections import defaultdict
from pathlib import Path
from typing import Dict, List


class DependencyGraph:
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)
        self.graph = defaultdict(list)

    def build(self) -> Dict[str, List[str]]:
        for path in self.workspace_root.rglob('*.py'):
            relative = str(path.relative_to(self.workspace_root))
            source = path.read_text(encoding='utf-8', errors='ignore')

            for line in source.splitlines():
                line = line.strip()

                if line.startswith('import ') or line.startswith('from '):
                    self.graph[relative].append(line)

        return dict(self.graph)
