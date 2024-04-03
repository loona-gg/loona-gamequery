# Loona OpenGSQ Python Library

A modified fork of [OpenGSQ](https://github.com/opengsq/opengsq-python) built for [Loona](https://loona.gg).

## Supported Protocols

The library supports a wide range of protocols. Here are some examples:

```py
from opengsq.protocols import (
    ASE,
    Battlefield,
    Doom3,
    EOS,
    FiveM,
    GameSpy1,
    GameSpy2,
    GameSpy3,
    GameSpy4,
    Kaillera,
    KillingFloor,
    Minecraft,
    Quake1,
    Quake2,
    Quake3,
    RakNet,
    Samp,
    Satisfactory,
    Scum,
    Source,
    TeamSpeak3,
    Unreal2,
    Vcmp,
    WON,
    Terraria,
    Palworld,
)
```

## Requirements

- Python 3.7 or higher

## Installation

```sh
pip install -U git+https://github.com/loona-gg/loona-gamequery.git
```

## Usage

Here’s an example of how to query a server using the Source protocol:

```py
import asyncio
from opengsq.protocols import Source


async def main():
    source = Source(host='45.147.5.5', port=27015)
    info = await source.get_info()
    print(info)


asyncio.run(main())
```

## Credits

- [OpenGSQ](https://github.com/opengsq/opengsq-python)
- [GameServerMonitor](https://github.com/DiscordGSM/GameServerMonitor)