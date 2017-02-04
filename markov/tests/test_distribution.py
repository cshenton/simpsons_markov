from markov.chain import Distribution

dist = Distribution('foo')
dist.update('foo')
dist.update('foo')
dist.update('bar')
dist.update('bar')

def test_prob():
    assert dist.targets['foo'] == 0.6
    assert dist.targets['bar'] == 0.4

def test_obs():
    assert dist.obs == 5

def test_choose():
    sample = [dist.choose() for _ in range(100000)]
    assert round(len([x for x in sample if x=='foo'])/10000) == 6
    assert round(len([x for x in sample if x=='bar'])/10000) == 4
