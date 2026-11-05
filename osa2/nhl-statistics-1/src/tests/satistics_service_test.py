import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaajat(self):
        nimet = [player.name for player in self.stats._players]

        self.assertEqual(
            nimet,
            ["Semenko", "Lemieux", "Kurri", "Yzerman", "Gretzky"]
        )

    def test_pelaajat(self):
        pelaajat = self.stats.team("EDM")
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(
            nimet,
            ["Semenko", "Kurri", "Gretzky"]
        )
    
    def test_pelaajat_eiole(self):
        pelaajat = self.stats.team("EI")
        nimet2 = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(
            nimet2,
            []
        )

    def test_pelaaja_nimi(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        
    def test_pelaaja_nimi_ei_ole(self):
        pelaaja = self.stats.search("Essi")
        self.assertIsNone(pelaaja)

    def test_top(self):
        pelaajat = self.stats.top(2)
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(
            nimet,
            ["Gretzky", "Lemieux", "Yzerman"]
        )