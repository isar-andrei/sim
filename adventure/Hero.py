from adventure.Character import Character


class Hero(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.health = super().assign_status_value(70, 100)
        self.strength = super().assign_status_value(70, 80)
        self.defence = super().assign_status_value(45, 55)
        self.speed = super().assign_status_value(40, 50)
        self.luck = super().assign_status_value(10, 30)
