# Simpsons Plot Synopsis Generator

This is an implementation of a markov chain text generator in python, used to generate plot synopses for *The Simpsons*. The implentation is pretty unstable (read: *hilarious*)

## Example Synopses

> Bart gets in trouble when he kisses the enigmatic daughter of two lawyers, while Lisa is a terrorist.

> Mr. Burns goes on forever.

> While Homer tries to make big money, Bart fails at his job of taking care of Grandpa, and Lisa stay with them until he gains access to Chief Wiggum's master key to the Simpson family, but their newfound happiness is threatened when the convict escapes from prison and runs away from home, winds up costing Mr. Burns accidentally swallows Maggie and the two of them.

> Homer is disappointed when the western he rented turns out to be a human skeleton with wings.

> Mr. Burns is sent to prison for art theft, where a scary inmate introduces him to go all-out to get Homer to create folk art figures.
Homer must do one good deed to get Homer to start a swear jar to stop them from destroying the future.

## Usage

Simply run `python3 scrape_simpsons.py` from root to scrape all imdb simpsons synopses, generate a markov chain, and use that markov chain to produce 10 new simpsons plot summaries.

## /markov

This is a source agnostic markov chain trainer. It implements a `Chain` class, which exposes methods for processing blocks of text.

