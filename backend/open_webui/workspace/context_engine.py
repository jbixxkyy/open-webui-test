from typing import Dict, List


class ContextEngine:
    def build_context(self, query: str, files: List[Dict]):
        ranked_files = []

        for file in files:
            score = 0

            if query.lower() in file.get('path', '').lower():
                score += 1

            ranked_files.append(
                {
                    'file': file,
                    'score': score,
                }
            )

        ranked_files.sort(key=lambda item: item['score'], reverse=True)

        return {
            'query': query,
            'matches': ranked_files[:20],
        }
