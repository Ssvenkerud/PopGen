import logging

import pandas as pd


class Population_config:
    """
    Class holding the population information
    """

    def __init__(self):
        self.population = pd.DataFrame()
        self.n = 0

    def get_population(self):
        """
        function for returning the population
        """
        return self.population

    def set_parameters(self, number_of_people: int = 0):
        """
        method to sett the parameters for the populations
        :param number_of_people: int
        """
        try:
            self.n = int(number_of_people)
            logging.info(f"number_of_people set to: {number_of_people}")
        except:
            logging.warning(
                f"number_of_people parameter {number_of_people} not convertable, sett"
                " to 0"
            )
            self.n = int(0)
