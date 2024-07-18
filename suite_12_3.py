import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def setUp(cls):
        cls.r1 = Runner('Усэйн', 10)
        cls.r2 = Runner('Андрей', 9)
        cls.r3 = Runner('Ник', 3)

    @classmethod
    def tear_DownClass(cls):
        result_names = {place: runner.name for place, runner in cls.all_results.items()}
        print(f"{result_names}")


    def testers_runs_1(self):
        trn = Tournament(90, self.r1, self.r3)
        self.results = trn.start()
        self.all_results.update(self.results)
        last_place = max(self.results.keys())
        self.assertTrue(self.results[last_place].name == 'Ник')
        self.tear_DownClass()

    def testers_runs_2(self):
        trn = Tournament(90, self.r2, self.r3)
        self.results = trn.start()
        self.all_results.update(self.results)
        last_place = max(self.results.keys())
        self.assertTrue(self.results[last_place].name == 'Ник')
        self.tear_DownClass()
    def testers_runs_3(self):
        trn = Tournament(90, self.r1, self.r2, self.r3)
        self.results = trn.start()
        self.all_results.update(self.results)
        last_place = max(self.results.keys())
        self.assertTrue(self.results[last_place].name == 'Ник')
        self.tear_DownClass()

if __name__ == '__main__':
    unittest.main()
