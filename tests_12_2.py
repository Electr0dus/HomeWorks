import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r = Runner('Test1')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = Runner('Test2')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r1 = Runner('Test3')
        r2 = Runner('Test3')
        for i in range(10):
            r1.walk()
        for i in range(10):
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()
