import pandas as pd

from src.simple_generator import SimpleGenerator


def test_simple_generater_init():
    population_size = 5
    schema = {"integer": "int"}
    SimpleGenerator_init = SimpleGenerator(population_size, schema)
    assert isinstance(SimpleGenerator_init, SimpleGenerator)
    assert hasattr(SimpleGenerator_init, "population_size")
    assert hasattr(SimpleGenerator_init, "schema")
    assert hasattr(SimpleGenerator_init, "data")


def test_run():
    population_size = 5
    schema = {"integer": "int", "float": "float"}
    pop = SimpleGenerator(population_size, schema)
    result = pop.run()
    assert len(result) == population_size
    assert isinstance(result, pd.DataFrame)
    assert result.columns.values.tolist() == [*schema]


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
