from opengsq.protocols.palworld import Palworld


async def main():
    proto = Palworld(host="63.143.62.98", port=8221)
    print(await proto.query())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
