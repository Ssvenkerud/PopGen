import pytest
from src.Schema import *

def test_schema_blank_init():
    schema = Schema()
    assert isinstance(schema, Schema)