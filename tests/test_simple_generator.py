import random

import numpy
import pandas as pd

from src.simple_generator import SimpleGenerator


def test_simple_generater_init():
    population_size = 5
    schema = {"integer": "int"}
    simplegenerator_init = SimpleGenerator(population_size, schema)
    assert isinstance(simplegenerator_init, SimpleGenerator)
    assert hasattr(simplegenerator_init, "population_size")
    assert hasattr(simplegenerator_init, "schema")
    assert hasattr(simplegenerator_init, "data")


def test_multi_column_generation():
    population_size = 5
    schema = {"integer": "int", "float": "float", "category": "cat"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert len(result) == population_size
    assert isinstance(result, pd.DataFrame)
    assert result.columns.values.tolist() == [*schema]
    assert result["integer"].dtype == numpy.dtype("int64")
    assert result["float"].dtype == numpy.dtype("float64")
    assert type(result["category"].values.all()) == str


def test_integer_column_type():
    population_size = 5
    schema = {"integer": "int"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert isinstance(result, pd.DataFrame)
    assert max(result["integer"]) <= 100
    assert min(result["integer"]) >= 0


def test_integer_column_min_max_value():
    population_size = 5
    schema = {"integer": "int"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert max(result["integer"]) <= 100
    assert min(result["integer"]) >= 0


def test_float_column_type():
    population_size = 5
    schema = {"float": "float"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert isinstance(result, pd.DataFrame)


def test_float_column_min_max_value():
    population_size = 5
    schema = {"float": "float"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert max(result["float"]) <= 1
    assert min(result["float"]) >= 0


def test_categorical_column_type():
    population_size = 5
    schema = {"cat": "categorical"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert isinstance(result, pd.DataFrame)
