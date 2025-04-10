from app.db.connection import get_db_connection
from fastapi import APIRouter, HTTPException, status
from app.models.schema import TechStack, TechStackCreate
from app.crud.tech_stack import create_tech_stack, get_all_tech_stacks

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
    
@router.get("/", response_model=list[TechStack], status_code=status.HTTP_200_OK)
async def get_all_tech_stacks_endpoint():
    """
    Endpoint to get all tech stack entries from the database
    """

    connection = await get_db_connection()
    try:
        tech_stacks = await get_all_tech_stacks()
        return tech_stacks
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
            )
    finally:
        await connection.close()
