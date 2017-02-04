class Chain:
    def __init__(self, depth):
        self.token_hash = {}
        self.depth = depth

    def update(self, token, result):
        """
        token: a tuple of strings of lenth `self.depth`
        result: a string

        updates the token hash based on the token - result pair
        """
        pass

    def simulate(self, start=None):
        """
        start: a token in the Chain's token_hash to start with

        generates a string based on the
        """
        pass
