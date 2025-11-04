class Student:
    def __init__(self, name, roll_no, scores):
        self.name = name
        self.roll_no = roll_no
        self.scores = scores  # Dictionary like {'Math': 80, 'Science': 75, 'English': 90}

    def average(self):
        return sum(self.scores.values()) / len(self.scores)

    def status(self):
        return "Pass" if all(score >= 33 for score in self.scores.values()) else "Fail"