import random

import pandas as pd
import numpy

from src.simple_generator import SimpleGenerator


def test_simple_generater_init():
    population_size = 5
    schema = {"integer": "int"}
    simplegenerator_init = SimpleGenerator(population_size, schema)
    assert isinstance(simplegenerator_init, SimpleGenerator)
    assert hasattr(simplegenerator_init, "population_size")
    assert hasattr(simplegenerator_init, "schema")
    assert hasattr(simplegenerator_init, "data")


def test_run():
    population_size = 5
    schema = {"integer": "int", "float": "float", "category": "cat"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert len(result) == population_size
    assert isinstance(result, pd.DataFrame)
    assert result.columns.values.tolist() == [*schema]
    assert result["integer"].dtype == numpy.dtype('int64')
    assert result["float"].dtype == numpy.dtype('float64')
    assert type(result["category"].values.all()) == str


def test_integer_column():
    population_size = 5
    schema = {"integer": "int"}
    pop = SimpleGenerator(population_size, schema)
    result = pop._integer_column("integer", 0, 100)
    assert type(result) == dict
    assert max(result["integer"]) <= 100
    assert min(result["integer"]) >= 0


def test_float_column():
    population_size = 5
    schema = {"float": "float"}
    pop = SimpleGenerator(population_size, schema)
    result = pop._float_column("float", 0, 1)
    assert type(result) == dict
    assert max(result["float"]) <= 1
    assert min(result["float"]) >= 0


def test_categorical_column():
    population_size = 5
    schema = {"cat": "categorical"}
    pop = SimpleGenerator(population_size, schema)
    categories = ["one", "two", "three"]
    result = pop._categorical_column("cat", categories)
    assert type(result) == dict
    assert random.choice(result["cat"]) in categories
    assert random.choice(result["cat"]) != "four"
