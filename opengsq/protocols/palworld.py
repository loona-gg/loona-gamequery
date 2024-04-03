import os
import time
from typing import TYPE_CHECKING

import aiohttp
from opengsq.protocol_socket import Socket

from opengsq.protocol_base import ProtocolBase


class Palworld(ProtocolBase):
    full_name = "Palworld Protocol"

    async def query(self):
        ip = await Socket.gethostbyname(self._host)

        base_url = os.getenv('OPENGSQ_MASTER_SERVER_URL', 'https://master-server.opengsq.com/').rstrip('/')
        url = f"{base_url}/palworld/search?host={ip}&port={self._port}"
        start = time.time()

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data: dict = await response.json()
                ping = int((time.time() - start) * 1000)

        result = {
            "name": data.get("name", ""),
            "map": data.get("map_name", ""),
            "password": data.get("is_password", False),
            "numplayers": data.get("current_players", 0),
            "numbots": 0,
            "maxplayers": data.get("max_players", 0),
            "players": None,
            "bots": None,
            "connect": f"{self._host}:{self._port}",
            "ping": ping,
            "raw": data,
        }

        return result
