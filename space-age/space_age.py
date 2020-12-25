class SpaceAge:
    EARTH_ORBITAL_PERIOD = 31557600
    RATIOS = (
        ("earth", 1),
        ("mercury", 0.2408467),
        ("venus", 0.61519726),
        ("mars", 1.8808158),
        ("jupiter", 11.862615),
        ("saturn", 29.447498),
        ("uranus", 84.016846),
        ("neptune", 164.79132),
    )

    def __init__(self, seconds: int):
        if seconds <= 0:
            raise ValueError("A positive non zero number of seconds must be provided")
        self.seconds = seconds

        self.PERIODS = (
            (planet, SpaceAge.EARTH_ORBITAL_PERIOD * ratio)
            for planet, ratio in SpaceAge.RATIOS
        )
        for planet, period in self.PERIODS:
            setattr(self, "on_" + planet, lambda p=period: round(self.seconds / p, 2))
