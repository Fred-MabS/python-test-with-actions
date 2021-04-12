import src.json_generator as CUT
import pytest
import json
from jsonschema import validate, ValidationError

@pytest.fixture
def metadata_schema():
    with open('./json_schemas/metadata_schema.json') as schema_file:
        return json.load(schema_file)

def test_correct(metadata_schema):
    try:
        validate(instance=CUT.correct(), schema=metadata_schema)
    except:
        pytest.fail()

def test_incorrect(metadata_schema):
    try:
        validate(instance=CUT.incorrect(), schema=metadata_schema)
    except ValidationError as e:
        pytest.fail()

