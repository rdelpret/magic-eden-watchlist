import os
import yaml


def get_config():
    '''
    helper func to parse configfile
    '''

    # TODO add some safety here
    watchlist_dir = os.path.dirname(
        os.path.realpath(__file__)) + "/../watchlist.yaml"


    with open(watchlist_dir, "r") as f:
        config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return config
