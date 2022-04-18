import logging
import random

import pandas as pd


class SimpleGenerator:
    def __init__(self, population_size: int, schema: dict):
        logging.info("init simple generator")
        self.population_size = population_size
        self.schema = schema
        self.data = None
        logging.debug(f"init population size: {self.population_size}")
        logging.debug(f"init schema: {self.schema}")
        logging.debug(f"init data values: {self.data}")

    def _integer_column(
        self, column_name: str, min_value: int = 0, max_value: int = 100
    ):
        logging.info(f"creating integer column: {column_name}")
        logging.debug(f"min value:{min_value}")
        logging.debug(f"max_value: {max_value}")

        column_value = []
        for _ in range(0, self.population_size):
            n = random.randint(min_value, max_value)
            column_value.append(n)
        column = {column_name: column_value}

        return column

    def _float_column(self, column_name: str, min_value: int = 0, max_value: int = 1):
        logging.info(f"creating float column: {column_name}")
        logging.debug(f"min value:{min_value}")
        logging.debug(f"max_value: {max_value}")
        column_value = []
        for _ in range(0, self.population_size):
            n = random.uniform(min_value, max_value)
            column_value.append(n)
        column = {column_name: column_value}

        return column

    def _categorical_column(self, column_name: str, categories: list):
        column_value = []
        for _ in range(0, self.population_size):
            n = random.choice(categories)
            column_value.append(n)
        column = {column_name: column_value}

        return column

    def run(self):
        data = {}
        for k, v in self.schema.items():
            if v == "int":
                col = self._integer_column(k)
                data.update(col)
            elif v == "float":
                col = self._float_column(k)
                data.update(col)
            elif v == "cat":
                col = self._categorical_column(k)
                data.update(col)

        self.data = pd.DataFrame.from_dict(data)

        return self.data
