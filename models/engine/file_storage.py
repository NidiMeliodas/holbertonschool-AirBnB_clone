#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
import json

"""FileStorage est un fichier où se trouvent les fonctions pour travailler avec la désérialisation et
la sérialisation"""


class FileStorage:
    """La classe FileStorage est chargée des méthodes de stockage de fichiers"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Une fonction qui renvoie le dictionnaire __objects"""
        return self.__objects

    def new(self, obj):
        """Une fonction qui définit dans __objects l'objet avec la clé
        <nom de la classe de l'objet>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Une fonction qui sérialise __objects dans le fichier JSON
        (chemin : __file_path)"""
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Une fonction qui : désérialise le fichier JSON vers
        __objects (uniquement si le fichier JSON (__file_path) existe ;
        sinon, ne fait rien."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
