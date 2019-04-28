import asyncio
import aiohttp
from fpl import FPL


class FplSession:
    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.session = aiohttp.ClientSession()
        self.fpl = FPL(self.session)

    async def login(self):
        await self.fpl.login(self.email, self.password)

    async def close(self):
        await self.session.close()
