from numpy.random import choice

class Distribution:
    """
    Represents the distribution of results for a particular token
    """
    def __init__(self, value):
        self.targets = {value: 1.0}
        self.obs = 1

    def update(self, new_value):
        """
        Updates the distribution of values given the newly observed value
        """
        for k,v in self.targets.items():
            if k == new_value:
                self.targets[k] = (self.obs*v + 1)/(self.obs + 1)
            else:
                self.targets[k] = (self.obs*v)/(self.obs + 1)

        if new_value not in self.targets.keys():
            self.targets[new_value] = 1 / (self.obs + 1)

        self.obs += 1

    def choose(self):
        """
        Randomly select a value according to the target probability distibution
        """
        outcome = choice(list(self.targets.keys()),
                         p=list(self.targets.values()))
        return outcome

class Chain:
    def __init__(self, depth):
        self.token_hash = {}
        self.depth = depth

    def update(self, new_token, value):
        """
        new_token: a tuple of strings of lenth `self.depth`
        value: a string

        updates the token hash based on the token - value pair
        """
        if new_token in self.token_hash.keys():
            token_hash[new_token].update(value)
        else:
            token_hash[new_token] = Distribution(value)


    def simulate(self, start=None):
        """
        start: a token in the Chain's token_hash to start with

        generates a string based on the
        """
        pass
