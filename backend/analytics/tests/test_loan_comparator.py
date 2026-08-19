from django.test import SimpleTestCase
from analytics.engines.loan_comparator import compare_loans

class LoanComparatorTests(SimpleTestCase):
    def test_comparison(self):
        result = compare_loans(100000, 12)
        self.assertTrue(result)
        self.assertLessEqual(result[0]["total_repayment"], result[-1]["total_repayment"])
