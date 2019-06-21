

class Todo:
    def __init__(self, name, description, deadline, priority, done_status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.done_status = done_status

    def to_string(self):
        line = " | ".join([self.name, self.description,
                           self.deadline, self.priority, self.done_status])
        return "".join([line, "\n"])
