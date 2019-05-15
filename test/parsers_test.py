from app.parsers import task_parser


def test_task_parser():
    # case command not provided
    command, value = task_parser("todo  ")
    assert command is None
    assert value is None

    command, value = task_parser("todo")
    assert command is None
    assert value is None

    command, value = task_parser("todos")
    assert command is None
    assert value is None

    # case show task
    command, value = task_parser("todo show")
    assert command == "show"
    assert value is None

    command, value = task_parser("todo show  ")
    assert command == "show"
    assert value is None

    command, value = task_parser("Todo show dddssa")
    assert command == "show"
    assert value == "dddssa"

    # case add task
    command, value = task_parser("todo add go to the market")
    assert command == "add"
    assert value == "go to the market"

    command, value = task_parser("todo add ล้างจาน")
    assert command == "add"
    assert value == "ล้างจาน"

    command, value = task_parser("todo  ADD")
    assert command == "add"
    assert value is None

    # case delete task
    command, value = task_parser("todo del 3")
    assert command == "del"
    assert value == "3"

    command, value = task_parser("todo del -3")
    assert command == "del"
    assert value == "-3"