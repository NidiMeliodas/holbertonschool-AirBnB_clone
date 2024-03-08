import json


class FileStorage:
    """Classe pour la gestion du stockage des fichiers"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Renvoie le dictionnaire __objects"""
        return self.__objects

    def new(self, obj):
        """Ajoute l'objet à __objects avec la clé <nom de la classe>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Sérialise __objects en JSON et écrit dans le fichier"""
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Désérialise le fichier JSON en __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    class_name = key.split(".")[0]
                    # Vous devrez importer la classe dynamiquement ici
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
