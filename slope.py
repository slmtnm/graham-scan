from __future__ import annotations
from fractions import Fraction


class Slope:
    def __init__(self, dx: int, dy: int) -> None:
        self.dx, self.dy = dx, dy

    def to_fraction(self) -> Fraction:
        return Fraction(self.dy, self.dx)
    
    def __lt__(self, other: Slope) -> bool:
        if self.dx > 0 and other.dx < 0:
            return True
        if self.dx < 0 and other.dx > 0:
            return False

        if self.dx * other.dx > 0:
            return self.to_fraction() < other.to_fraction()
        
        if self.dx == 0:
            if other.dx == 0:
                return False
            return other.dx < 0

        if other.dx == 0:
            if self.dx == 0:
                return False
            return self.dx > 0
        
        raise Exception("Case not covered")
    

    def __eq__(self, other: Slope) -> bool:
        if self.dx * other.dx < 0:
            return False

        if self.dx * other.dx > 0:
            return self.to_fraction() == other.to_fraction()

        return self.dx == 0 and other.dx == 0