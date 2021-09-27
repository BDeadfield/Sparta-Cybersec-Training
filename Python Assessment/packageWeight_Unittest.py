import unittest
import packageWeight


class MyTestCase(unittest.TestCase):
    def testPackageWeight(self):
        self.assertEqual(packageWeight.solve(128, 68, 251, 61), "rejected")
        self.assertEqual(packageWeight.solve(28, 268, 157, 50), "rejected")
        self.assertEqual(packageWeight.solve(100, 100, 100, 74), "rejected")
        self.assertEqual(packageWeight.solve(47, 33, 21, 74), "special")
        self.assertEqual(packageWeight.solve(299, 144, 73, 46), "special")
        self.assertEqual(packageWeight.solve(47, 33, 21, 50), "special")
        self.assertEqual(packageWeight.solve(91, 78, 65, 34), "standard")
        self.assertEqual(packageWeight.solve(99, 99, 99, 11), "standard")
        self.assertEqual(packageWeight.solve(14, 21, 34, 49), "standard")


if __name__ == "__main__":
    unittest.main()
