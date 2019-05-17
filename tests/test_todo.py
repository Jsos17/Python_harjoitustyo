import pytest
from src.todo import Todo


def test_to_string():
    todo = Todo("Task", "Urgent", "30.5.2019", "High", "Not done")
    assert todo.to_string() == "Task | Urgent | 30.5.2019 | High | Not done\n"
