
import aiosqlite as asql
from aiosqlite import Connection
from sqlite3 import Row

from misc.logger import logger


class Users:
    _db: Connection
    name = "./tgbot/models/users.dp"

    @classmethod
    async def get_table(cls):
        c = await cls._db.cursor()
        await c.execute("""SELECT id FROM userTable""")

        records: Row = await c.fetchall()
        return [str(el[0]) for el in records]

    @classmethod
    async def connect(cls):
        cls._db = await asql.connect(cls.name)
        c = await cls._db.cursor()
        await c.execute("""CREATE TABLE if not exists userTable (id INTEGER)""")
        await cls._db.commit()
        logger.info("Users DataBase was connected successfully!")

    @classmethod
    async def insert(cls, user_id: int) -> bool:
        c = await cls._db.cursor()

        await c.execute(f"""SELECT id FROM userTable WHERE id={user_id}""")
        records: Row = await c.fetchall()
        if not len(records) == 0:
            return False

        await c.execute(f"""INSERT INTO userTable (id) VALUES ({user_id})""")
        await cls._db.commit()
        return True


async def main():
    await Users.connect()
