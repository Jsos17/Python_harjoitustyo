import src.todo_logic as logic


def test_check_filename1():
    assert logic.check_filename("todo.txt") == False


def test_check_filename2():
    assert logic.check_filename("txt") == True


def test_file_ending():
    assert object.__eq__(logic.file_ending("tomorrow"), "rrow")


def test_todo_modify():
    line = "a | qw | e | r | t"
    inputs = ["", "d", "", "", "xx"]
    todo = logic.todo_modify(line, inputs)
    assert object.__eq__(todo.name, "a")
    assert object.__eq__(todo.description, "d")
    assert object.__eq__(todo.deadline, "e")
    assert object.__eq__(todo.priority, "r")
    assert object.__eq__(todo.done_status, "xx")


def test_get_index():
    assert logic.get_index(10, 2) == 2
    assert logic.get_index(10, "huh") == -3
    assert logic.get_index(10, 10) == -2
    assert logic.get_index(10, -1) == -1
