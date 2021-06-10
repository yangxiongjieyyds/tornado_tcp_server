# coding:utf-8

import os
import yaml

conf = None


def load_config():
    global conf
    path = os.path.dirname(__file__)
    conf_file = os.path.join(path, 'application.yaml')
    with open(conf_file, 'r', encoding='utf-8') as f:
        cont = f.read()
    conf = yaml.load(cont, Loader=yaml.SafeLoader)


if __name__ == '__main__':
    load_config()
    print(conf)
