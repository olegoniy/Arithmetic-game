import pytest
from game import Game

def test_name_setter():
    """Test that an empty name raises a ValueError"""
    with pytest.raises(ValueError, match="Empty name. Please try again!"):
        game = Game("")  # Should raise an error

def test_task_generator():
    """Test that task_generator produces valid results"""
    game = Game("Tester")
    ans, start = game.task_generator()
    assert isinstance(ans, int), "Answer should be an integer"
    assert isinstance(start, float), "Start time should be a float"

def test_score_initialization_and_increment():
    """Test that score starts at 0 and increments correctly"""
    game = Game("Tester")
    
    # Score should start at 0
    assert game.score == 0, "Initial score should be 0"
    
    # Simulate correct answer by manually increasing score
    game.score += 1
    assert game.score == 1, "Score should be 1 after one increment"
