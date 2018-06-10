from src.infra.data._db import DbManager


class RepositoryBase:
    def __init__(self, class_name):
        self.__db = DbManager.DB
        self.__session = DbManager.DB.session
        self.__class = class_name

    @property
    def db(self):
        return self.__db

    @property
    def session(self):
        return self.__session

    def get_by_id(self, _id):
        return DbManager.DB.session.query(self.__class).get(_id)

    def get_all(self):
        return DbManager.DB.session.query(self.__class).all()

    def save(self, entity, commit=True):
        self.session.add(entity)
        if commit:
            self.session.commit()

    def save_many(self, entities, commit=True):
        self.session.add_all(entities)
        if commit:
            self.session.commit()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def delete(self, entity, commit=True):
        if not entity:
            raise ValueError('Record is required to delete.')
        if not entity.id:
            raise ValueError('Id is required to delete.')

        obj_to_delete = self.get_by_id(entity.id)
        if obj_to_delete:
            self.session.delete(obj_to_delete)
            if commit:
                self.session.commit()
            return True
        else:
            return False
