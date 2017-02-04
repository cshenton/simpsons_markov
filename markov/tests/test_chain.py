from markov.chain import Chain

chain = Chain(2)

chain.add_passage('this is a sentence')

def test_depth():
    assert chain.depth == 2

def test_starts():
    assert chain.starts == [('this', 'is')]

def test_token_hash():
    assert ('this', 'is') in chain.token_hash.keys()
    assert chain.token_hash[('this', 'is')].targets['a'] == 1
    assert chain.token_hash[('a', 'sentence')].targets[None] == 1

def test_simulate():
    assert chain.simulate() == 'this is a sentence'.split()
