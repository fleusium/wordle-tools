IN = 'wordlist_300k.txt'
OUT = 'wordlist_len5_top40k.txt'


def main():
    words = []
    count = 0
    with open(IN, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            word = parts[0].strip()
            if len(word) == 5:
                # print(word)
                words.append(word)
                count += 1
            if count >= 10:
                pass
                # break
    print(f'Total 5-letter words: {count}')
    print('Saving...')
    with open(OUT, 'w', encoding='utf-8') as f_out:
        for w in words:
            f_out.write(w + '\n')


if __name__ == '__main__':
    main()
