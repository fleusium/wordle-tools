# Wordle tools
## Usage

`python suggest.py included_letters excluded_letters`

- Known positions of included_letters can be indicated by a number after the letter, e.g. "a2".
- Excluded positions of included_letters can be indicated by an exclamation mark, e.g. "a!2".

Usage examples:
```
wordle-tools> python suggest.py abc defghijklmno

First 6 out of 6 possibilities:
['crabs', 'scuba', 'scabs', 'cabby', 'abaca', 'bract']
```
or
```
wordle-tools> python suggest.py c1h2a3p!4

First 1 out of 1 possibilities:
['champ']
```


## Statistics
For some statistics (letter frequency, etc.) see `statistics.ipynb`.


## Word lists
- `wordle_list.txt`: Past solutions of Wordle. Useful for statistics.
- `wordlist_300k.txt`: 300k most used English words of all lengths.
- `wordlist_len5_top5k.txt`: 5k most used English words of five characters. This is recommended for `suggest.py`.
- `wordlist_len5_top40k.txt`: 40k most used English words of five characters, extracted from `wordlist_300k`.
