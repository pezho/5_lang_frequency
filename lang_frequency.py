
import re
from collections import Counter


def load_data(filepath):
    """В том случае если файл большой лучше читать его построчно"""
    pass


def get_most_frequent_words(filepath, minlen=0):
    """
    
    """
    worlds_count = Counter()
    for line in open(filepath, encoding='utf8'):
        line = re.sub(r'[,.!@#$%^&*()=+_?\/—]', '', line)
        for world in line.lower().split():
            if len(world) < minlen:
                continue
            worlds_count[world] += 1
            
    return worlds_count.most_common(10)


if __name__ == '__main__':
    filepath = 'РУСЛАН И ЛЮДМИЛА.txt'
    print('\n'.join(map(lambda w: '%s: %s' % w, get_most_frequent_words(filepath))))
