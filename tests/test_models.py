import pytest
from pydantic import ValidationError
from app.models import QuestSchema

def test_quest_schema_valid_creation():
    """Test A: Valid creation (happy path)"""
    data = {
        "name": "q-001",
        "category": "Mindfulness",
        "min_days": 3,
        "max_days": 5,
        "effort": 2
    }
    quest = QuestSchema(**data)
    assert quest.name == "q-001"
    assert quest.min_days == 3
    assert quest.max_days == 5

def test_quest_schema_invalid_range():
    """Test B: Invalid recurrence (max < min) raises ValidationError"""
    data = {
        "name": "q-002",
        "category": "Invalid Quest",
        "min_days": 10,
        "max_days": 5,
        "effort": 3
    }
    with pytest.raises(ValidationError) as exc_info:
        QuestSchema(**data)
    
    # Asserting the custom error message we wrote in the model
    assert "max_days (5) cannot be less than min_days (10)" in str(exc_info.value)