from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url='sqlite://dbo.db'
    )
    await Tortoise.generate_schemas()
k