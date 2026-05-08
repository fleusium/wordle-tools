import os

IN = 'wordle_list_raw.txt'
OUT = 'wordle_list.txt'

print(f'Processing {IN}...')

# return the first column of IN
words: list[str] = []
with open(IN, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(' ')
        word = parts[0].strip()
        words.append(word.lower())
print(f'Total words: {len(words)}')
print(f'Unique words: {len(set(words))}')

# delete old OUT file if exists
if os.path.exists(OUT):
    print(f'{OUT} already exists, deleting...')
    os.remove(OUT)

with open(OUT, 'w', encoding='utf-8') as f_out:
    for w in words:
        f_out.write(w + '\n')
print(f'Saving to {OUT}...')
