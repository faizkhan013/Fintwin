from django.test import SimpleTestCase
from analytics.engines.risk_engine import calculate_survivable_loss, calculate_delayed_payment_risk

class RiskEngineTests(SimpleTestCase):
    def test_survivable_loss(self):
        self.assertGreater(calculate_survivable_loss(100000, 70000, 50000), 0)
    def test_delayed_payment_risk(self):
        self.assertEqual(calculate_delayed_payment_risk(25000, 100000), 25)
