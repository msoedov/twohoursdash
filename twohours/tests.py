from unittest import expectedFailure
from django.test import TestCase
from .utils import bizzfuzz


class BuzzFizz(TestCase):

    def test_tree(self):
        self.assertEqual(bizzfuzz(3), 'Bizz')

    def test_five(self):
        self.assertEqual(bizzfuzz(5), 'Fuzz')

    def test_fifteen(self):
        self.assertEqual(bizzfuzz(15), 'BizzFuzz')

    def test_anything_else(self):
        self.assertEqual(bizzfuzz(8), 8)

    @expectedFailure
    def test_onefifty(self):
        self.assertEqual(bizzfuzz(150), 'Fuzz')