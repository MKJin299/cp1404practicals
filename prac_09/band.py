class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musicians list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing all musicians playing or needing an instrument."""
        return "\n".join(musician.play() for musician in self.musicians)