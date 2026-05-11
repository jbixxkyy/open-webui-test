from typing import Dict, List


class SemanticSearch:
    def __init__(self):
        self.documents: List[Dict] = []

    def index_document(self, payload: Dict):
        self.documents.append(payload)

    def search(self, query: str):
        results = []

        for document in self.documents:
            score = 0

            content = document.get('content', '').lower()

            if query.lower() in content:
                score += 1

            if score > 0:
                results.append({
                    'score': score,
                    'document': document,
                })

        results.sort(key=lambda item: item['score'], reverse=True)

        return results[:20]
