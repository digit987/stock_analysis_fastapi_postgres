from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData
from sqlalchemy.sql import text
from app.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("phone_number", String, nullable=False),
    Column("created_at", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
)
