from typing import Dict, List


class VectorStore:
    def __init__(self):
        self.documents: List[Dict] = []

    def add(self, document: Dict):
        self.documents.append(document)

    def query(self, query: str):
        results = []

        for document in self.documents:
            text = document.get('text', '').lower()

            if query.lower() in text:
                results.append(document)

        return results[:25]
