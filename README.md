This is an implementation of Markov Chains in python, with associate routins to generate sentences based on inspirational quotes.

each word is determined by a random function and it's two previous words.

each of the generated quotes are also checked against all actual quotes to prevent them from being too similar to the real ones. This is done using python's `difflib.SequenceMatcher` which implements a version of the 1980 pattern matching algorithm by Ratcliff and Obershelp.
