import json

def correct():
    data = { 'firstname': 'fred', 'age': 45, 'kids': ['paul', 'lise'] }
    return data

def incorrect():
    data = { 'firstname': 'fred', 'age': 45, 'kids': 'paul' }
    return data
