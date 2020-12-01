from adventure.Character import Character


class Skill:
    def __init__(self, name: str, user: Character):
        if not type(name) is str:
            raise TypeError("Skill name needs to be a string")
        if not len(name):
            raise TypeError("Skill name can't be blank")
        else:
            self.name = name
        self.user = user
