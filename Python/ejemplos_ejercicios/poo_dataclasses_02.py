"""
EJEMPLO DE @dataclasses
Demostrar como una clase con muchos atributos se pude descomponer en varias
clases y tener una mejor estructura
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field


def constrained_sum_sample_pos(n: int, total: int) -> list[int]:
    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


@dataclass
class CharacterTraits:
    strength: int = 0
    constitution: int = 0
    dexterity: int = 0
    intelligent: int = 0
    wisdown: int = 0
    charisma: int = 0

    @staticmethod
    def roll() -> CharacterTraits:  # esto se puede hacer por -annotations-
        print(constrained_sum_sample_pos)
        return CharacterTraits(*constrained_sum_sample_pos(6, 100))


@dataclass
class Player:
    name: str
    traits: CharacterTraits = field(default_factory=CharacterTraits.roll)
    health: int = 100
    xp: int = 0
    inventory: list[str] = field(default_factory=list)


def main():
    # player = Player(name="mack", traits=CharacterTraits(strength=10))
    player = Player(name="mack")

    print(f"player.name  --> {player.name}")
    print(f"player.health  --> {player.health}")
    print(f"player.xp  --> {player.xp}")
    print(f"player.inventory  --> {player.inventory}")
    print(f"player.traits.strength  --> {player.traits.strength}")
    print(f"player.traits.constitution  --> {player.traits.constitution}")
    print(f"player.traits.dexterity  --> {player.traits.dexterity}")
    print(f"player.traits.wisdown  --> {player.traits.wisdown}")
    print(f"player.traits.charisma  --> {player.traits.charisma}")

    print(f"player.__annotations__ --> {player.__annotations__}")


if __name__ == "__main__":
    main()
