from dataclasses import dataclass
@dataclass
class Tratta:

    _id_origine : int
    _id_destinazione : int
    _distanza : int

    @property
    def id_origine(self):
        return self._id_origine

    @property
    def id_destinazione(self):
        return self._id_destinazione

    @property
    def distanza(self):
        return self._distanza

    def __hash__(self):
        return hash(self._id_origine)
