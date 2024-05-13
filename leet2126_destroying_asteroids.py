class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        total_mass = mass

        for asteroid in asteroids:
            if asteroid > total_mass:
                return False
            else:
                total_mass += asteroid
        return True
