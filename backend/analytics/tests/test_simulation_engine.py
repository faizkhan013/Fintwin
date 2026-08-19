from django.test import SimpleTestCase
from analytics.engines.simulation_engine import simulate_shock

class SimulationTests(SimpleTestCase):
    def test_negative_shock_can_reduce_balance(self):
        result = simulate_shock(10000, 50000, 45000, income_reduction=30, expense_increase=10)
        self.assertIn("final_balance", result)
