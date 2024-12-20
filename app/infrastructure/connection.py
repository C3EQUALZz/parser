from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, create_async_engine

from app.settings.config import config

engine: AsyncEngine = create_async_engine(
    url=config.database.url,
    pool_pre_ping=config.alchemy.pool_pre_ping,
    pool_recycle=config.alchemy.pool_recycle,
    echo=config.alchemy.echo,
)

session_factory: async_sessionmaker = async_sessionmaker(
    bind=engine,
    autoflush=config.alchemy.auto_flush,
    expire_on_commit=config.alchemy.expire_on_commit
)
