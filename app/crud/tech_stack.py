import uuid
from app.db.connection import get_db_connection
from app.models.schema import TechStackCreate, TechStack
from app.db.tech_stack import CREATE_TECH_STACK

async def create_tech_stack(tech_stack: TechStackCreate) -> TechStack:
    """
    Create a new tech stack in the database
    """
    connection = await get_db_connection()
    tech_stack_id = uuid.uuid4()

    created = await connection.fetchrow(CREATE_TECH_STACK, tech_stack_id, tech_stack.name)

    return TechStack({
        "id": created["id"],
        "name": created["name"]
    })
