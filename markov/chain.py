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
        self.starts = []

    def update(self, new_token, value, start=False):
        """
        new_token: a tuple of strings of lenth `self.depth`
        value: a string

        updates the token hash based on the token - value pair
        """
        if len(new_token) != self.depth:
            # throw exception
            pass

        if new_token in self.token_hash.keys():
            token_hash[new_token].update(value)
        else:
            token_hash[new_token] = Distribution(value)

        if start:
            self.starts += [new_token]

    def add_passage(self, passage):
    """
    Updates the provided Chain with the supplied passage.
    """

    tokens = passage.split()
    token_dict = {}
    depth = self.depth

    for i in range(len(tokens)-depth+1):
        if i == 0:
            is_start = True

        if i < len(tokens)-depth:
            self.update(tuple(tokens[i:(i+depth)]), tokens[i+depth], is_start)
        else:
            self.update(tuple(tokens[i:(i+depth)]), None, is_start)

    def simulate(self, start=None):
        """
        start: a token in the Chain's token_hash to start with

        Generates a passage based on the Chains token hash
        """
        if start is None:
            current = choice(self.starts)
        elif start not in self.starts
            # later, throw exception
            current = choice(self.starts)
        else:
            current = start

        passage = list(current)
        new_string = self.token_hash[current].choose()

        while new_string is not None:
            passage += [new_string]
            current = tuple(passage[-depth:])
            new_string = self.token_hash[current].choose()

        return passage
