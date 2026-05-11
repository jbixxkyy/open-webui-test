from typing import Dict, List

from open_webui.workspace.symbol_extractor import SymbolExtractor


class SymbolSearch:
    def __init__(self, workspace_root: str):
        self.extractor = SymbolExtractor(workspace_root)

    def search(self, query: str) -> List[Dict]:
        symbols = self.extractor.extract_symbols()

        return [
            symbol
            for symbol in symbols
            if query.lower() in symbol['name'].lower()
        ]
