import ast
from pathlib import Path
from typing import Dict, List


class SymbolExtractor:
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)

    def extract_python_symbols(self, file_path: str) -> List[Dict]:
        path = self.workspace_root / file_path
        source = path.read_text(encoding='utf-8')
        tree = ast.parse(source)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                symbols.append({
                    'type': 'function',
                    'name': node.name,
                    'path': file_path,
                    'line': node.lineno,
                })

            if isinstance(node, ast.ClassDef):
                symbols.append({
                    'type': 'class',
                    'name': node.name,
                    'path': file_path,
                    'line': node.lineno,
                })

        return symbols

    def extract_symbols(self) -> List[Dict]:
        symbols = []

        for path in self.workspace_root.rglob('*.py'):
            relative = str(path.relative_to(self.workspace_root))

            try:
                symbols.extend(self.extract_python_symbols(relative))
            except Exception:
                continue

        return symbols
