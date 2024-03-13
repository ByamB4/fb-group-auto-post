from os import path
from json import load
import typing

SOCIAL_MAPS = {
    'facebook': {
        'login': 'https://m.facebook.com/login',
        'filename': 'facebook-cookies.json'
    }
}

PROJECT_ROOT = path.dirname(path.abspath(__name__))

def get_sources_list() -> typing.List:
    with open(f'{PROJECT_ROOT}/groups.json', 'r') as sources_file:
        return load(sources_file)