from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID

class TechStackBase(BaseModel):
    name: str

class TechStackCreate(TechStackBase): pass

class TechStack(TechStackBase):
    id: UUID

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    github_url: HttpUrl
    demo_url: Optional[HttpUrl]=None
    tech_stack_ids: List[UUID]=[]

class ProjectCreate(ProjectBase): pass

class Project(ProjectBase):
    id: UUID
    tech_stack: List[TechStack]=[]
    created_at: str
    updated_at: str