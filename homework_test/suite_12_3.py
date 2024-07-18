import unittest
import runner_test
import test_12_3


# 1 Часть
runST = unittest.TestSuite()

runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)

# 2 Часть
