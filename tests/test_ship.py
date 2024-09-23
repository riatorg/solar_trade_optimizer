import unittest
from solar_trade.ship import Ship

class TestShip(unittest.TestCase):
    
    def test_ship_initialization(self):
        # Test that a Ship object is initialized with the correct values
        ship = Ship(daily_cost=100.0, capacity=50)
        self.assertEqual(ship.daily_cost, 100.0)
        self.assertEqual(ship.capacity, 50)
    
    def test_calculate_total_cost(self):
        # Test that the total cost is calculated correctly
        ship = Ship(daily_cost=100.0, capacity=50)
        total_cost = ship.calculate_total_cost(days=10)
        self.assertEqual(total_cost, 1000.0)  # 100.0 * 10 days = 1000.0

if __name__ == "__main__":
    unittest.main()
