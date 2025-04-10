import os

from dotenv.main import load_dotenv
import asyncpg
from typing import Optional

load_dotenv()

db_uri = os.getenv("SUPABASE_URI")

async def get_db_connection() -> Optional[asyncpg.Connection]:
    """
    Description:
        Get the Supabase database connection.
    Returns:
        asyncpg.Connection: The database connection.
    """
    try:
        conn = await asyncpg.connect(db_uri)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None