from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional

class QuestSchema(BaseModel):
    name: str
    category: str
    effort: int = Field(..., ge=1, le=5)
    min_days: int = Field(default=1, ge=1)
    max_days: int = Field(default=7, ge=1)
    

    @model_validator(mode='after')
    def validate_days_range(self) -> 'QuestSchema':
        if self.max_days < self.min_days:
            raise ValueError(
                f"max_days ({self.max_days}) cannot be less than min_days ({self.min_days})"
            )
        return self