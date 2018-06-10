import json
import uuid


class EntityBase:

    @staticmethod
    def get_id(_id=None):
        return uuid.uuid4().hex if _id is None else _id

    def as_json(self):
        return self.__dict__
