from pydantic import BaseModel


class TaskCreate(BaseModel):
    url: str


class TaskOut(BaseModel):
    id: int
    url: str
    status: str
    result: str | None

    class Config:
        orm_mode = True
