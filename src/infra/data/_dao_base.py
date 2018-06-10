from src.infra.data._db import DbManager


class DaoBase:
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

    def save_many(self, entities, commit=True): # TODO: Remove this method after implements automatic VOs updates
        self.session.add_all(entities)
        if commit:
            self.session.commit()

    def delete(self, entity, commit=True): # TODO: Remove this method after implements automatic VOs updates
        self.session.delete(entity)
        if commit:
            self.session.commit()
