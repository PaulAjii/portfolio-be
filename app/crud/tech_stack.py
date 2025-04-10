from app.db.connection import get_db_connection
from app.models.schema import TechStackCreate, TechStack
from app.db.tech_stack import CREATE_TECH_STACK, GET_ALL_TECH_STACKS

async def create_tech_stack(tech_stack: TechStackCreate) -> TechStack:
    """
    Create a new tech stack in the database
    """
    connection = await get_db_connection()

    created = await connection.fetchrow(CREATE_TECH_STACK, tech_stack.name)

    return TechStack(
        name = created["name"],
        id = created["id"]
    )

async def get_all_tech_stacks() -> list[TechStack]:
    """
    Get all tech stacks from the database
    """
    connection = await get_db_connection()

    tech_stacks = await connection.fetch(GET_ALL_TECH_STACKS)

    return [TechStack(
        id = tech_stack["id"],
        name = tech_stack["name"]
    ) for tech_stack in tech_stacks]
