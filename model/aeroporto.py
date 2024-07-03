from dataclasses import dataclass
@dataclass
class Aeroporto:

    _id: int
    _nome: str

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    def __hash__(self):
        return hash(self._id)