import asyncio
from typing import AsyncGenerator


class TerminalStream:
    async def stream(self, generator) -> AsyncGenerator[str, None]:
        while True:
            output = generator()

            if output:
                yield output

            await asyncio.sleep(0.05)
