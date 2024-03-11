from models import Note
from sqlalchemy.ext.asyncio import async_sessionmaker,AsyncSession
from sqlalchemy import select
class CRUD:

    async def get_all(self, async_sessionmaker: async_sessionmaker[AsyncSession]):
        async with async_sessionmaker() as session:
            statement = select(Note).order_by(Note.id)
            result = await session.execute(statement)
            return result.scalars()
    
    async def create(self, async_sessionmaker: async_sessionmaker[AsyncSession],note: Note):
        async with async_sessionmaker() as session:
            session.add(note)
            await session.commit()
        return note

    # async def read(self, **kwargs):
    #     return await Note.query.where(**kwargs).gino.all()

    async def get_by_id(self, async_sessionmaker: async_sessionmaker[AsyncSession],note_id: str):
        async with async_sessionmaker() as session:
            statement = select(Note).filter(Note.id == note_id)
            result = await session.execute(statement)
            return result.scalar()
        
    async def update(
        self, async_session: async_sessionmaker[AsyncSession], note_id:str, data
    ):
        """
        Update note by id
        """
        async with async_session() as session:
            statement = select(Note).filter(Note.id == note_id)

            result = await session.execute(statement)

            note = result.scalar()

            note.title = data['title']
            note.content = data['content']

            await session.commit()
            return note
        

    async def delete(self, async_session: async_sessionmaker[AsyncSession], note: Note):
        """delete note by id
        """
        async with async_session() as session:
            await session.delete(note)
            await session.commit()

        return {}