This is an implementation of Markov Chains in python, with associate routins to generate sentences based on inspirational quotes.

A markov chain is built based on the statistical relations between words in the refrence quotes. In the new sentences, each word is determined by a weighted random choice baised on it's two previous words.

each of the generated quotes are also checked against all actual quotes to prevent them from being too similar to the real ones. This is done using python's `difflib.SequenceMatcher` which implements a version of the 1980 pattern matching algorithm by Ratcliff and Obershelp.

See [this page](aestuans.github.io/Inspirotron/) for the results.
