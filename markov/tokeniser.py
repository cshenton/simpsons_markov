def tokenise(passage, depth):
    """
    passage: a passage of text to split into markov chain token - result pairs
    depth: how many words/punctuation, should be in each token

    Returns a dict of token - result pairs, where a result of None
    denotes the end of a passage of text.
    """

    tokens = passage.split()
    token_dict = {}

    for i in range(len(tokens)-depth+1):
        if i < len(tokens)-depth:
            token_dict[tuple(tokens[i:(i+depth)])] = tokens[i+depth]
        else:
            token_dict[tuple(tokens[i:(i+depth)])] = None

    return token_dict
