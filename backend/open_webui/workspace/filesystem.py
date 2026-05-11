from pathlib import Path
from typing import List


class WorkspaceFileSystem:
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)

    def _resolve_path(self, file_path: str) -> Path:
        return self.workspace_root / file_path

    def list_files(self) -> List[str]:
        files = []

        for path in self.workspace_root.rglob('*'):
            if path.is_file():
                files.append(str(path.relative_to(self.workspace_root)))

        return sorted(files)

    def read_file(self, file_path: str) -> str:
        path = self._resolve_path(file_path)
        return path.read_text(encoding='utf-8')

    def write_file(self, file_path: str, content: str):
        path = self._resolve_path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

        return {
            'success': True,
            'path': file_path,
        }

    def create_file(self, file_path: str):
        path = self._resolve_path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

        return {
            'success': True,
            'path': file_path,
        }

    def create_folder(self, folder_path: str):
        path = self._resolve_path(folder_path)
        path.mkdir(parents=True, exist_ok=True)

        return {
            'success': True,
            'path': folder_path,
        }

    def rename_path(self, old_path: str, new_path: str):
        source = self._resolve_path(old_path)
        target = self._resolve_path(new_path)

        source.rename(target)

        return {
            'success': True,
            'old_path': old_path,
            'new_path': new_path,
        }

    def delete_file(self, file_path: str):
        path = self._resolve_path(file_path)

        if path.exists():
            path.unlink()

        return {
            'success': True,
            'path': file_path,
        }
