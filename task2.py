import unittest
from task1 import get_score


class TestGetScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        score1 = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 1, "score": {"home": 0, "away": 1}},
            {"offset": 2, "score": {"home": 0, "away": 2}},
            {"offset": 3, "score": {"home": 1, "away": 2}},
        ]
        answer1 = {
            0: {"home": 0, "away": 0},
            1: {"home": 0, "away": 1},
            2: {"home": 0, "away": 2},
            3: {"home": 1, "away": 2},
        }
        score2 = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 2, "score": {"home": 0, "away": 1}},
            {"offset": 4, "score": {"home": 0, "away": 2}},
            {"offset": 6, "score": {"home": 1, "away": 2}},
        ]
        answer2 = {
            0: {"home": 0, "away": 0},
            1: {"home": 0, "away": 0},
            2: {"home": 0, "away": 1},
            3: {"home": 0, "away": 1},
            4: {"home": 0, "away": 2},
            5: {"home": 0, "away": 2},
            6: {"home": 1, "away": 2},
        }
        score3 = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 3, "score": {"home": 0, "away": 1}},
            {"offset": 6, "score": {"home": 0, "away": 2}},
            {"offset": 9, "score": {"home": 1, "away": 2}},
        ]
        answer3 = {
            0: {"home": 0, "away": 0},
            1: {"home": 0, "away": 0},
            2: {"home": 0, "away": 0},
            3: {"home": 0, "away": 1},
            4: {"home": 0, "away": 1},
            5: {"home": 0, "away": 1},
            6: {"home": 0, "away": 2},
            7: {"home": 0, "away": 2},
            8: {"home": 0, "away": 2},
            9: {"home": 1, "away": 2},
        }
        score4 = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 3, "score": {"home": 0, "away": 1}},
            {"offset": 4, "score": {"home": 0, "away": 2}},
            {"offset": 6, "score": {"home": 1, "away": 2}},
        ]
        answer4 = {
            0: {"home": 0, "away": 0},
            1: {"home": 0, "away": 0},
            2: {"home": 0, "away": 0},
            3: {"home": 0, "away": 1},
            4: {"home": 0, "away": 2},
            5: {"home": 0, "away": 2},
            6: {"home": 1, "away": 2},
        }
        score5 = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 5, "score": {"home": 0, "away": 1}},
            {"offset": 10, "score": {"home": 0, "away": 2}},
            {"offset": 10, "score": {"home": 1, "away": 2}},
        ]
        answer5 = {
            0: {"home": 0, "away": 0},
            1: {"home": 0, "away": 0},
            2: {"home": 0, "away": 0},
            3: {"home": 0, "away": 0},
            4: {"home": 0, "away": 0},
            5: {"home": 0, "away": 1},
            6: {"home": 0, "away": 1},
            7: {"home": 0, "away": 1},
            8: {"home": 0, "away": 1},
            9: {"home": 0, "away": 2},
            10: {"home": 1, "away": 2},
        }

        cls.scores_set = [
            (score1, answer1),
            (score2, answer2),
            (score3, answer3),
            (score4, answer4),
            (score5, answer5),
        ]

    def test_negative_offset(self):
        offset = -10
        for i, score_set in enumerate(self.scores_set, 1):
            score, answer = score_set
            with self.subTest(scoreset=i):
                self.assertDictEqual(get_score(score, offset), answer[0])

    def test_zero_offset(self):
        offset = 0
        for i, score_set in enumerate(self.scores_set, 1):
            score, answer = score_set
            with self.subTest(scoreset=i):
                self.assertDictEqual(get_score(score, offset), answer[0])

    def test_offset_after_end_game(self):
        offset = 10000
        for i, score_set in enumerate(self.scores_set, 1):
            score, answer = score_set
            with self.subTest(scoreset=i):
                self.assertDictEqual(get_score(score, offset), answer[max(answer.keys())])

    def test_all_offset(self):
        for i, score_set in enumerate(self.scores_set, 1):
            score, answer = score_set
            with self.subTest(scoreset=i):
                for offset in answer.keys():
                    with self.subTest(offset=offset):
                        self.assertDictEqual(get_score(score, offset), answer[offset])
