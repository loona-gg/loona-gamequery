import os
import time
from typing import TYPE_CHECKING

import aiohttp
from opengsq.protocol_socket import Socket

from opengsq.protocol_base import ProtocolBase
from opengsq.responses.models import ServerStatus, PlayersList


class Palworld(ProtocolBase):
    full_name = "Palworld Protocol"

    async def query(self):
        ip = await Socket.gethostbyname(self._host)

        base_url = os.getenv('OPENGSQ_MASTER_SERVER_URL', 'https://master-server.opengsq.com/').rstrip('/')
        url = f"{base_url}/palworld/search?host={ip}&port={self._port}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data: dict = await response.json()

        result = ServerStatus(
            name=data.get("name", ""),
            description=data.get("map_name", ""),
            players_list={
                "online": data.get("current_players", 0),
                "max": data.get("max_players", 0),
                "list": [],
            },
        )

        return result
