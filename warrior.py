class Warrior:
    def __init__(self, name, maximum_health):
        self.name = name
        self.maximum_health = maximum_health
        self.is_alive = True

    def __add__(self, other):
        if self.is_alive and other.is_alive:
            new_name = f"{self.name} {other.name}"
            new_max_health = self.maximum_health + other.maximum_health
            return Warrior(name=new_name, maximum_health=new_max_health)
        else:
            return None

    def __sub__(self, other):
        if self.is_alive and other.is_alive:
            self.maximum_health -= 1
            other.maximum_health -= 1

            if self.maximum_health <= 0:
                self.is_alive = False

            if other.maximum_health <= 0:
                other.is_alive = False

    def __str__(self):
        return f'Warrior(name="{self.name}", maximum_health={self.maximum_health}, is_alive={self.is_alive})'


xena = Warrior(name="Xena", maximum_health=1)
print(str(xena))  # 'Warrior(name="Xena", maximum_health=1, is_alive=True)'

conan = Warrior(name="Barbar Conan", maximum_health=2)
print(xena.is_alive)  # True
print(conan.is_alive)  # True

child = xena + conan
print(child.is_alive)  # True
print(child.name)  # "Xena Barbar Conan"
print(child.maximum_health)  # 3

fight = xena - conan
print(fight)  # None
print(xena.is_alive)  # False
print(conan.is_alive)  # True
print(str(xena))  # 'Warrior(name="Xena", maximum_health=1, is_alive=False)'

child_2 = xena + conan
print(child_2)  # None
