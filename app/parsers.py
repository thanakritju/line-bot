import re


def task_parser(message):
    task_regex = re.compile(r'[tT]odo\s+([a-zA-Z]+)?\s*(.+)?')
    command, value = task_regex.match(message).groups()
    if command:
        return command.lower(), value
    return None, None