from enum import Enum


class QuestionType(str, Enum):
    SELECT = 'SELECT'
    NUM = 'NUM'
    NORMAL = 'NORMAL'
