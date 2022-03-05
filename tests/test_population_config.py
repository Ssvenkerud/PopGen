import pandas as pd
import numpy as np
import logging
from src.Population_config import Population_config


def test_Population_classinit():
    assert isinstance(Population_config(), Population_config)
    population_init = Population_config()
    assert isinstance(population_init, Population_config)
    assert hasattr(population_init, "population")
    assert isinstance(population_init.population, pd.DataFrame)
    assert population_init.population.empty
    assert hasattr(population_init, "n")
    assert type(population_init.n) == int


def test_set_population_param():
    n = 5
    pop = Population_config()
    pop.set_parameters(n)
    assert pop.n == n
    assert type(pop.n) == int


def test_get_population():
    population = Population_config()
    assert hasattr(population, "get_population")
    result = population.get_population()
    assert isinstance(result, pd.DataFrame)


def test_set_population_param_n_typing():
    number_of_people = [5, 10000, None, np.nan, "10", 15.3]
    for n in number_of_people:
        pop = Population_config()
        pop.set_parameters(n)
        assert type(pop.n) == int


def test_logger(caplog):
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Testing now.")
    pop = Population_config()
    pop.set_parameters(None)
    assert "number_of_people parameter None not convertable, sett to 0" in caplog.text
