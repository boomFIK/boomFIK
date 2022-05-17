with open('lyrics.txt', encoding="utf8") as f:
    lyrics = f.read()

lyrics_list = []
banned = [' ','.',',','!','?']
lyrics_word = ''

for w in lyrics:
    w = w.lower()
    if w == '\n':
        if lyrics_word:
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    elif w not in banned:
        lyrics_word += w
    else:
        if lyrics_word:
            lyrics_list.append(lyrics_word)
        lyrics_word = ''


if lyrics_word:
    lyrics_list.append(lyrics_word)
    lyrics_word = ''

check_dupes = {}


for w in lyrics_list:
    w = w.lower()
    if w not in check_dupes:
        check_dupes[w] = 1

    else:
        check_dupes[w] += 1

most_freq_word = max(check_dupes.values())


for k in check_dupes.keys():
    if check_dupes[k] == most_freq_word:
        most_freq_word = k, check_dupes[k]
        break

print(f'Most frequent word in sentence is: {most_freq_word[0]} - {most_freq_word[1]}')

def most_common_words(freq):
    values = freq.values()
    best = max(values)
    words = []
    for k in freq:
        if freq[k] == best:
            words.append(k)
    return words, best


def words_often(freq, times):
    result = []
    done = False
    while not done:
        temp = most_common_words(freq)
        if temp[1] >= times:
            result.append(temp)
            for w in temp[0]:
                del(freq[w])
        else:
            done = True
    return result

lyrics_2000 = words_often(check_dupes, 5)

print(lyrics_2000)


