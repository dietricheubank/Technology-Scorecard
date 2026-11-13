import unittest
from history import Snapshot,analyze_trend
class TrendTests(unittest.TestCase):
    def test_higher_better(self):
        r=analyze_trend([Snapshot("2026-09",95),Snapshot("2026-10",97)],96,"up")
        self.assertEqual(r["trend"],"improving")
        self.assertTrue(r["on_target"])
    def test_lower_better(self):
        r=analyze_trend([Snapshot("2026-09",4),Snapshot("2026-10",3)],2,"down")
        self.assertEqual(r["trend"],"improving")
        self.assertFalse(r["on_target"])
    def test_duplicates(self):
        with self.assertRaises(ValueError):
            analyze_trend([Snapshot("x",1),Snapshot("x",2)],1,"up")
if __name__=="__main__": unittest.main()
