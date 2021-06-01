from time import time

from opengsq.interfaces import IServer
from opengsq.models import Player, Server
from opengsq.protocols import GS3


class BF2(IServer):
    full_name = 'Battlefield 2'

    def __init__(self, address: str, query_port: int, timeout: float = 5.0):
        super().__init__(address, query_port)
        self.protocol = GS3(address, query_port, timeout)

    async def query(self) -> Server:
        start_time = time()
        response = await self.protocol.get_info()
        latency = time() - start_time

        info = response['info']

        s = Server()
        s.ip = self.address
        s.query_port = self.query_port
        s.game_port = int(info['hostport'])
        s.name = info['hostname']
        s.map = info['mapname']
        s.password = info['password'] == '1'
        s.players = int(info['numplayers'])
        s.max_players = int(info['maxplayers'])
        s.bots = sum(player['AIBot_'] == '1' for player in response['player_'])
        s.player_list = []
        s.latency = latency
        s.raw = response

        for player in response['player_']:
            p = Player()
            p.name = player['player_'].strip()
            p.score = int(player['score_'])
            p.time = 0
            s.player_list.append(p)

        return s