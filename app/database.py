from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from databases import Database
from app.config import settings
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Function to create the database if it doesn't exist
def create_database_if_not_exists():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT 1 FROM pg_database WHERE datname = '{settings.DATABASE_NAME}'"
        )
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f"CREATE DATABASE {settings.DATABASE_NAME}")
            print(f"Database '{settings.DATABASE_NAME}' created.")
        else:
            print(f"Database '{settings.DATABASE_NAME}' already exists.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")
        raise

# Using `create_async_engine` for asynchronous operations
async_engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Creating a sessionmaker for async use
async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)

# Initializing the Database instance for async operations
database = Database(settings.DATABASE_URL)

# Metadata for creating tables
from sqlalchemy import MetaData
metadata = MetaData()

# Function to create tables asynchronously
async def create_tables():
    from app.models import metadata  # Ensure models are imported
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

# Invoking the function to ensure the database exists
create_database_if_not_exists()
