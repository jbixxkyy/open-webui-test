from pathlib import Path
from typing import List


class WorkspaceFileSystem:
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)

    def list_files(self) -> List[str]:
        files = []

        for path in self.workspace_root.rglob('*'):
            if path.is_file():
                files.append(str(path.relative_to(self.workspace_root)))

        return files

    def read_file(self, file_path: str) -> str:
        path = self.workspace_root / file_path
        return path.read_text(encoding='utf-8')

    def write_file(self, file_path: str, content: str):
        path = self.workspace_root / file_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def delete_file(self, file_path: str):
        path = self.workspace_root / file_path

        if path.exists():
            path.unlink()
