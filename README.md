# Simpsons Plot Synopsis Generator

This is an implementation of a markov chain text generator in python, used to generate plot synopses for *The Simpsons*

## Usage

Simply run `python3 scrape_simpsons.py` from root to scrape all imdb simpsons synopses, generate a markov chain, and use that markov chain to produce 10 new simpsons plot summaries.

## /markov

This is a source agnostic markov chain trainer. It implements a `tokeniser`, designed to parse a free form string into token - result pairs, and a `Chain` class, which is trained of token - result pairs, and can produced simulated sentences.

