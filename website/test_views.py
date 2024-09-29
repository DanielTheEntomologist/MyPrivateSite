
from django.test import TestCase
from django.urls import reverse
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class viewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.sluggless_urls = [
    'home',
    'aboutme',
    'post',
    'category',
    ]

    def test_url_responses(self):
        for url in self.sluggless_urls:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 200)

class testNavigation(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_navigation_to_pages_fire(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.LINK_TEXT, "About Me").click()
        self.assertIn("http://localhost:8000/aboutme", self.driver.current_url)

        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        self.assertIn("http://localhost:8000/home", self.driver.current_url)

    def test_navigation_to_categories_fire(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.LINK_TEXT, "Categories").click()    
        self.driver.find_element(By.LINK_TEXT, "Test Driven Development").click()
        self.assertIn("http://localhost:8000/category/tdd-with-aoc/", self.driver.current_url)

        self.driver.find_element(By.LINK_TEXT, "Categories").click()    
        self.driver.find_element(By.LINK_TEXT, "This Site").click()
        self.assertIn("http://localhost:8000/category/this-site/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()