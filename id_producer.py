from typing import Type, Dict, Set


class IdProducer:
    __idSet: Dict[Type, Set[int]]
    __max_id: Dict[Type, int]

    def __init__(self):
        self.__max_id = {}
        self.__idSet = {}

    def produce(self, cls: Type):
        self.__max_id.setdefault(cls, 0)
        self.__idSet.setdefault(cls, {0})

        if len(self.__idSet[cls]) != 0:
            return self.__idSet[cls].pop()
        else:
            self.__max_id[cls] += 1
            return self.__max_id[cls]

    def ret_id(self, rid: int, cls: Type):
        self.__idSet[cls].add(rid)
