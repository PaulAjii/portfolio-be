from app.db.connection import get_db_connection
from fastapi import APIRouter, HTTPException, status
from app.models.schema import TechStack, TechStackCreate
from app.crud.tech_stack import create_tech_stack

router = APIRouter(prefix="/tech_stack", tags=["Tech Stack"])

@router.post("/", response_model=TechStack, status_code=status.HTTP_201_CREATED)
async def create_tech_stack_endpoint(tech_stack: TechStackCreate):
    """
    Endpoint to create a new tech stack entry in the database
    """
    connection = await get_db_connection()
    try:
        new_tech_stack = await create_tech_stack(tech_stack)
        return new_tech_stack
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
            )
    finally:
        await connection.close()
