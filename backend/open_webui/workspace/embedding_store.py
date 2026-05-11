from typing import Dict, List


class EmbeddingStore:
    def __init__(self):
        self.embeddings: List[Dict] = []

    def add_embedding(self, payload: Dict):
        self.embeddings.append(payload)

    def similarity_search(self, query: str):
        results = []

        for item in self.embeddings:
            text = item.get('text', '').lower()

            if query.lower() in text:
                results.append(item)

        return results[:20]
