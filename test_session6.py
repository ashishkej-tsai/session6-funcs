import subprocess
import sys
import random



import pytest
import session6
from session6 import deck_function, deck_single_expression
import time
import os.path
import re
import inspect 

README_CONTENT_CHECK_FOR = [
    'lambda',
    'map',
    'filter',
    'doc',
    'string',
    'annotation'
]

deck_gt = [('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('6', 'spades'), ('7', 'spades'), ('8', 'spades'), ('9', 'spades'), 
           ('10', 'spades'), ('jack', 'spades'), ('queen', 'spades'), ('king', 'spades'), ('ace', 'spades'), 
           ('2', 'clubs'), ('3', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('6', 'clubs'), ('7', 'clubs'), ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs'), 
           ('jack', 'clubs'), ('queen', 'clubs'), ('king', 'clubs'), ('ace', 'clubs'), 
           ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'), ('6', 'hearts'), ('7', 'hearts'), ('8', 'hearts'), ('9', 'hearts'), 
           ('10', 'hearts'), ('jack', 'hearts'), ('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts'), 
           ('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'), 
           ('9', 'diamonds'), ('10', 'diamonds'), ('jack', 'diamonds'), ('queen', 'diamonds'), ('king', 'diamonds'), ('ace', 'diamonds')]


def test_single_expression():
    assert set(deck_single_expression) == set(deck_gt), "single expression output is wrong"

def test_normal_function():
    assert set(deck_function()) == set(deck_gt), "normal function output is wrong"

def test_func_docstring():
    assert "spades" in deck_function.__doc__, "doc string does not exists"

def test_func_annotations():
    assert "vals" in deck_function.__annotations__, "annotation does not exist"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

    
def test_fourspace():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

