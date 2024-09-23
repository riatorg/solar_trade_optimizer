class Ship:
    def __init__(self, daily_cost: float, capacity: int):
        """
        Initialize the Ship with a daily operational cost and a transport capacity.
        
        :param daily_cost: The daily cost of operating the ship (e.g., fuel, crew, maintenance).
        :param capacity: The total number of units the ship can transport.
        """
        self.daily_cost = daily_cost
        self.capacity = capacity

    def calculate_total_cost(self, days: int) -> float:
        """
        Calculate the total operational cost for a given number of days.
        
        :param days: Number of days the ship operates (e.g., number of days spent traveling between solar systems).
        :return: Total operational cost.
        """
        return self.daily_cost * days

    def __repr__(self):
        return f"Ship(daily_cost={self.daily_cost}, capacity={self.capacity})"

    def __str__(self):
        return f"Ship with daily cost of {self.daily_cost} and capacity of {self.capacity} units"
