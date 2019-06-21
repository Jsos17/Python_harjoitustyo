import src.todo_logic as logic


def test_check_filename1():
    assert logic.check_filename("todo.txt") == False


def test_check_filename2():
    assert logic.check_filename("txt") == True


def test_file_ending():
    assert logic.file_ending("tomorrow") == "rrow"


def test_todo_modify():
    line = "a | qw | e | r | t"
    inputs = ["", "d", "", "", "xx"]
    todo = logic.todo_modify(line, inputs)
    assert todo.name == "a"
    assert todo.description == "d"
    assert todo.deadline == "e"
    assert todo.priority == "r"
    assert todo.done_status == "xx"


def test_get_index():
    assert logic.get_index(10, 2) == 2
    assert logic.get_index(10, "huh") == -3
    assert logic.get_index(10, 10) == -2
    assert logic.get_index(10, -1) == -1
