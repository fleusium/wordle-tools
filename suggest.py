from dataclasses import dataclass, field
from typing import Optional
from pathlib import Path

import click


DEFAULT_WORDLIST_PATH = 'wordlist_len5_top5k.txt'
# DEFAULT_WORDLIST_PATH = 'wordlist_len5_top40k.txt'


# TODO
# separate click and logic
# UI


@dataclass
class Char:
    char: str = ''
    pos: Optional[int] = None
    pos_excludes: list[int] = field(default_factory=list)


@click.command()
@click.argument('includes', default='')
@click.argument('excludes', default='')
@click.option('--n', '-n', default=10, help='Number of suggestions')
@click.option('--wordlist-path', '-w', default=DEFAULT_WORDLIST_PATH, help='Path to wordlist file')
def suggest(
        includes: str | list[Char] = '',
        excludes: str | list[Char] = '',
        n: int = 10,
        wordlist: Optional[list[str]] = None,
        wordlist_path: Optional[str | Path] = DEFAULT_WORDLIST_PATH,
        ) -> list[str]:
    
    if isinstance(includes, str):
        includes = parse(includes)
    if isinstance(excludes, str):
        excludes = parse(excludes)

    if wordlist is None and wordlist_path is not None:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            wordlist = [line.strip() for line in f.readlines()]
    if wordlist is None:
        raise ValueError('Either wordlist or wordlist_path must be provided')
    
    suggested_items = []
    includes_str = ''.join([char.char for char in includes])
    for word in wordlist:
        if all(char.char in word for char in includes) and not any(char.char in word for char in excludes):
            if any(includes_str.count(char) > word.count(char) for char in set(includes_str)):
                # skip words that don't have enough occurrences of included letters
                continue
            if any(char.pos is not None and word[char.pos] != char.char for char in includes):
                # position-based includes
                continue
            if any(any(pos_excl is not None and word[pos_excl] == char.char for pos_excl in char.pos_excludes) for char in includes):
                # position-based excludes
                continue
            suggested_items.append(word)
            if len(suggested_items) >= n:
                pass
                # break

    n_suggested = min(n, len(suggested_items))

    print()
    print(f'First {n_suggested} out of {len(suggested_items)} possibilities:')
    print(suggested_items[:n_suggested])
    print()
    return suggested_items


def parse(string: str) -> list[Char]:
    """Parse a string like 'a1b2c!3d!123' into a list of Char objects."""
    
    # lowercase and remove spaces
    string = ''.join([s.lower() for s in string if s.strip()])
    if len(string) == 1 and not string[0].isalpha():
            # special case: ignore this argument
            return []

    chars: list[str] = []
    ch = ''
    for char in string:
        if char.isalpha():
            if ch:
                chars.append(ch)
            ch = char
        else:
            ch += char
    if ch:
        chars.append(ch)
    
    chars_obj: list[Char] = []
    for char in chars:
        ch = Char(char[0])
        s = char[1:]
        if '!' in s and not s.startswith('!'):
            raise ValueError(f'Invalid format: {char}')
        if '!' not in s and len(s) > 1:
            raise ValueError(f'Invalid format: {char}')
        if '!' not in s:
            ch.pos = int(s) - 1 if s.isdigit() else None
        else:
            ch.pos_excludes = [int(p) - 1 for p in s[1:] if p.isdigit()]
        chars_obj.append(ch)
    return chars_obj
    # return [char for char in string if char.isalpha()]


if __name__ == '__main__':
    suggest()
    pass
