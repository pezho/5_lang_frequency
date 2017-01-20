import re


def load_data(filepath):
    with open(filepath) as f:
        return f.read()


def get_most_frequent_words(text):
    WORLD_COUNT = 10
    worlds = {}
    for world in text.lower().split():
        world = re.sub(r'[,.!@#$%^&*()=+_?\/—:;]', '', world)
        if world:
            worlds[world] = worlds.get(world, 0) + 1
            
    return sorted(worlds.items(), key=lambda k: k[1], 
                                    reverse=True)[:WORLD_COUNT]


if __name__ == '__main__':
    filepath = input('Enter path to file: ')
    text = load_data(filepath)
    # print(text)
    most_frequent_words = get_most_frequent_words(text)
    for k, v in most_frequent_words:
        print('{}: {}'.format(k, v))

    
