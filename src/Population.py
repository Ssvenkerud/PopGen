import logging

import pandas as pd

from src.simple_generator import SimpleGenerator


class Population:
    """
    Class holding the population information
    """

    def __init__(self):
        self.data = pd.DataFrame()
        self.n = 0
        self.schema = None
        # TODO: Parameter for generation model
        # TODO: Change to initialise with parameters

    def get_population(self):
        """
        function for returning the population
        """
        return self.data

    def set_parameters(self, number_of_people: int = 0):
        """
        method to sett the parameters for the populations
        :param number_of_people: int
        """
        # TODO: Rewrite to be an update function, with rerun
        try:
            self.n = int(number_of_people)
            logging.info(f"number_of_people set to: {number_of_people}")
        except(TypeError):

            logging.warning(
                f"number_of_people parameter {number_of_people} not convertable, sett"
                " to 0"
            )
            self.n = int(0)

    def generate(self, schema):
        model = SimpleGenerator(self.n, schema)
        self.data = model.run()
