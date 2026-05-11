from pathlib import Path


class WorkspaceManager:
    def __init__(self, workspace_root: str = '.'):
        self.workspace_root = Path(workspace_root)

    def get_workspace_root(self):
        return str(self.workspace_root.resolve())

    def set_workspace_root(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)

        return {
            'success': True,
            'workspace_root': str(self.workspace_root.resolve())
        }
