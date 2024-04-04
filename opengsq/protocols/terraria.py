import json
import time
from typing import TYPE_CHECKING

import aiohttp

from opengsq.protocol_base import ProtocolBase
from opengsq.responses.models import ServerStatus


class Terraria(ProtocolBase):
    full_name = "terraria"

    def __init__(self, host: str, port: int, token: str, timeout: float = 5.0):
        self._token = token
        super().__init__(host, port, timeout)

    async def query(self):
        url = f"http://{self._host}:{self._port}/v2/server/status?players=true&rules=false&token={self._token}"
        start = time.time()

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                end = time.time()

        result = {
            "name": data["name"],
            "map": data["world"],
            "password": data["serverpassword"],
            "numplayers": len(data["players"]),
            "numbots": 0,
            "maxplayers": data["maxplayers"],
            "players": [
                {"name": player["nickname"], "raw": player}
                for player in data["players"]
            ],
            "bots": None,
            "connect": f"{self._host}:{data['port']}",
            "ping": int((end - start) * 1000),
            "raw": data,
        }
        print(json.dumps(result, indent=4))

        result = ServerStatus(
            name=result["name"],
            description=result["world"],
            players_list={
                "online": result["playercount"],
                "max": result["maxplayers"],
                "list": [{"id": x, "name": x} for x in result["players"]],
            },
        )

        return result
