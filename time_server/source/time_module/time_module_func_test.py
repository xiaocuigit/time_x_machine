from pprint import pprint
from time_server.source.time_module.time_normalizer import TimeNormalizer

if __name__ == '__main__':
    time_normalizer = TimeNormalizer()
    pprint("=====test=====")
    while True:
        sentence = input()
        pprint(time_normalizer.parse(sentence))
