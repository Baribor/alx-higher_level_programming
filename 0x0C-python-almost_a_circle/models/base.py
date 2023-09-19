#!/usr/bin/python3


class Base:
    __nb_objects = 0

    def __init__(self, id=None):

        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0:
            return '[]'
        json = ['[']
        c = 0
        d = 0

        for dictionary in list_dictionaries:
            json.append(', ' if d > 0 else "")
            json.append('{')
            for k, v in dictionary.items():
                json.append(f'{", " if c > 0 else ""}"{k}": {v}')
                c += 1
            json.append('}')
            c = 0
            d += 1

        json.append(']')
        return ''.join(json)

    @classmethod
    def save_to_file(cls, list_objs):
        list_of_dict = []
        for obj in list_objs:
            list_of_dict.append(obj.to_dictionary())

        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(Base.to_json_string(list_of_dict))
