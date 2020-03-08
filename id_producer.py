class IdProducer:
    def __init__(self):
        self.max_id = 0
        self.idSet = {0}

    def produce(self):
        if len(self.idSet) != 0:
            return self.idSet.pop()
        else:
            self.max_id += 1
            return self.max_id

    def ret_id(self, rid: int):
        self.idSet.add(rid)