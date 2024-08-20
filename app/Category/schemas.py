from pydantic import BaseModel, Field


class SCategory(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str = Field(..., min_length=1, max_length=100, description="Название, от 1 до 100 символов")
    description: str = Field(..., description="Описание")


class SCategoryAdd(BaseModel):
    name: str = Field(..., description="Название категории")
    description: str = Field(None, description="Описание категории")



class SCategoryUpd(BaseModel):
    name: str = Field(..., description="Новое название категории")
    description: str = Field(None, description="Новое описание категории")