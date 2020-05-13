from django.test import TestCase, LiveServerTestCase
from django.db import models
from .models import Room, Player
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized
import unittest
from .weatherscraper import WeatherScraper


class RoomModelTest(unittest.TestCase):
    room=Room.objects.get(id=1)
    @parameterized.expand([
        ["room name", room._meta.get_field('room_name').verbose_name],
        ["room desc", room._meta.get_field('room_desc').verbose_name],
        ["room c1", room._meta.get_field('room_c1').verbose_name],
        ["room c2", room._meta.get_field('room_c2').verbose_name],
        ["room c3", room._meta.get_field('room_c3').verbose_name],
        ["room c1 a", room._meta.get_field('room_c1_a').verbose_name],
        ["room c2 a", room._meta.get_field('room_c2_a').verbose_name],
        ["room c3 a", room._meta.get_field('room_c3_a').verbose_name],
        ["room desc alt", room._meta.get_field('room_desc_alt').verbose_name],
        ["room back", room._meta.get_field('room_back').verbose_name],
    ])

    def test_sequence(self, x, y):
        self.assertEquals(x,y)


class PlayerModelTest(unittest.TestCase):
    Player.objects.create(player_name = "johndoe", player_pass="password", player_lvl="Lake")
    player=Player.objects.get(id=1)
    @parameterized.expand([
        ["player name", player._meta.get_field('player_name').verbose_name],
        ["player pass", player._meta.get_field('player_pass').verbose_name],
        ["player lvl", player._meta.get_field('player_lvl').verbose_name],
    ])

    def test_sequence(self, x, y):
        self.assertEquals(x,y)


class WeatherTest(unittest.TestCase):
    ws = WeatherScraper()
    wc = ws.getData()
    @parameterized.expand([
        [wc, ""],
        [wc, None],
    ])

    def test_sequence(self, x,y):
        self.assertNotEquals(x,y)


class SeleniumTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SeleniumTestCase, self).tearDown()
    
    def test_game(self):
        selenium=self.selenium
        selenium.get('http://127.0.0.1:8000/')
        new_game = selenium.find_element_by_link_text('Start new game!')
        new_game.send_keys(Keys.RETURN)
        next_screen = selenium.find_element_by_link_text("There is a sign that says 'Exit' on a door to your left and a faint scent of fish coming from it")
        next_screen.send_keys(Keys.RETURN)
        next_screen = selenium.find_element_by_link_text("To you right you see a water well along the shore of the lake")
        next_screen.send_keys(Keys.RETURN)
        next_screen = selenium.find_element_by_link_text("Go down the well because you never follow safe programming techniques, in fact, you miss Limewire")
        next_screen.send_keys(Keys.RETURN)
        next_screen = selenium.find_element_by_link_text("Head towards the fountain full of thirst quenching Sprite Cranberry")
        next_screen.send_keys(Keys.RETURN)
        next_screen = selenium.find_element_by_link_text("Follow that creaky sound...after you try some Sprite Cranberry")
        next_screen.send_keys(Keys.RETURN)
        assert "You won!" in selenium.page_source
