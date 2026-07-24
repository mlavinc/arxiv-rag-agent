import asyncio

from app.services.vector_db.vector_db_service import vector_db_service


async def main():

    before = await vector_db_service.count()

    print(
        "Before reset:",
        before,
    )

    await vector_db_service.reset()

    after = await vector_db_service.count()

    print(
        "After reset:",
        after,
    )


asyncio.run(main())