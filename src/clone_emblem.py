class Stats:
    """Culmination of numbers that makes up units' attack and defenses 
    used in determining attack power in battle
    
    Class Attributes:
        e
    """
    #TODO: define tables for levelling up
    
    def __init__(self, level, health, attack, speed, defense, resistance) -> None:
        self.level = level
        self.health = health
        self.attack = attack
        self.speed = speed
        self.defense = defense
        self.resistance = resistance
    
    def level_up(self) -> None:
        """Increses stats based on current level and level up table
        """

class Weapon:
    """Battle weapon used to attack with.
    Adds attack power and possibly extra stats to a unit depending on weapon abilities
    
    """
    
    def __init__(self) -> None:
        self.name = ""
        self.might = 0
        self.range = 0
        self.effective = []
        self.extra_stats = {}

class Skill:
    """Extra attributes added to unit, allies, or foes, that benefit the unit in some way
    
    Class Attributes
    """
    
    def __init__(self) -> None:
        self.name = ""
        self.type = ""

class Unit:
    """Battle unit with set of stats and attributes used to attack, debuff, or aid other units
    
    Class attributes:
        e
    """
    def __init__(self, name: str, stats: Stats, weapon: Weapon, skills: list[Skill]) -> None:
        self.name = name
        self.stats = stats
        self.weapon = weapon
        self.skills = skills
