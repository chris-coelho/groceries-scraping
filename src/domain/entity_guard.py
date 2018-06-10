from abc import ABCMeta, abstractmethod


class EntityGuard(metaclass=ABCMeta):
    ISSUES = []

    def __init__(self):
        EntityGuard.clear_issues()

    @abstractmethod
    def check(self, entity):
        pass

    @classmethod
    def clear_issues(cls):
        cls.ISSUES = []

    @classmethod
    def add_issue(cls, issue):
        cls.ISSUES.append(issue)

    @classmethod
    def get_issues(cls):
        return cls.ISSUES

