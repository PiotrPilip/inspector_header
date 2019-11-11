import os


class ParsedFile:
    def __init__(self, location, filename):
        self.location = location
        self.filename = filename

    def __str__(self):
        return str(os.path.join(self.location, self.filename))