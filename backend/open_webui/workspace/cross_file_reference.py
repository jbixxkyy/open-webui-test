from collections import defaultdict
from pathlib import Path
from typing import Dict, List


class CrossFileReference:
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)

    def build(self) -> Dict[str, List[str]]:
        references = defaultdict(list)

        files = list(self.workspace_root.rglob('*.*'))

        for source in files:
            try:
                source_text = source.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                continue

            for target in files:
                if source == target:
                    continue

                target_name = target.stem

                if target_name in source_text:
                    references[str(source.relative_to(self.workspace_root))].append(
                        str(target.relative_to(self.workspace_root))
                    )

        return dict(references)
