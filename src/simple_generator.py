import random

import pandas as pd


class SimpleGenerator:
    def __init__(self, population_size: int, schema: dict):
        self.population_size = population_size
        self.schema = schema
        self.data = None

    def _integer_column(
        self, column_name: str, min_value: int = 0, max_value: int = 100
    ):
        column_value = []
        for _ in range(0, self.population_size):
            n = random.randint(min_value, max_value)
            column_value.append(n)
        column = {column_name: column_value}

        return column

    def _float_column(self, column_name: str, min_value: int = 0, max_value: int = 1):
        column_value = []
        for _ in range(0, self.population_size):
            n = random.uniform(min_value, max_value)
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

        self.data = pd.DataFrame.from_dict(data)

        return self.data
