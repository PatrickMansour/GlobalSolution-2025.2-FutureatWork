from typing import Dict


class Competence:
    """Representa uma única competência com um nome e um nível (0-5)."""

    def __init__(self, name: str, level: int = 0):
        self.name = name
        self.level = max(0, min(5, int(level)))

    def __repr__(self):
        return f"Competence(name={self.name!r}, level={self.level})"


class Profile:
    """Representa um perfil profissional que engloba competências técnicas e comportamentais."""

    def __init__(self, name: str):
        self.name = name
        self.technical: Dict[str, int] = {}
        self.behavioral: Dict[str, int] = {}

    def set_technical(self, comp_name: str, level: int):
        self.technical[comp_name] = max(0, min(5, int(level)))

    def set_behavioral(self, comp_name: str, level: int):
        self.behavioral[comp_name] = max(0, min(5, int(level)))

    def to_dict(self):
        return {
            "name": self.name,
            "technical": dict(self.technical),
            "behavioral": dict(self.behavioral),
        }

    @classmethod
    def from_dict(cls, data: dict):
        p = cls(data.get("name", "Anônimo"))
        p.technical = dict(data.get("technical", {}))
        p.behavioral = dict(data.get("behavioral", {}))
        return p

    def __repr__(self):
        return f"Profile(name={self.name!r}, technical={self.technical}, behavioral={self.behavioral})"


class Career:
    """Representa uma carreira com as competências necessárias e uma breve descrição.

As competências necessárias são representadas como dicionários que mapeiam nome -> nível desejado.
    """

    def __init__(self, name: str, req_tech: Dict[str, int], req_beh: Dict[str, int], description: str = ""):
        self.name = name
        self.required_technical = dict(req_tech)
        self.required_behavioral = dict(req_beh)
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "required_technical": dict(self.required_technical),
            "required_behavioral": dict(self.required_behavioral),
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get("name", "Desconhecido"),
            data.get("required_technical", {}),
            data.get("required_behavioral", {}),
            data.get("description", ""),
        )

    def __repr__(self):
        return f"Career(name={self.name!r})"
