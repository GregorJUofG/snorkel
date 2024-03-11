from enum import Enum

class Experience(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    EXPERT = 3

Experience = Enum('Experience', ['BEGINNER', 'INTERMEDIATE', 'EXPERT'])
