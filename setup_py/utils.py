from contextlib import contextmanager
from appdata import AppDataPaths
from configparser import ConfigParser


@contextmanager
def config_parser():
    app_data_paths = AppDataPaths(
        app_name='opensource',
        with_dot=True
    )
    if app_data_paths.require_setup():
        app_data_paths.setup()
    config_parser = ConfigParser()
    config_parser.read(app_data_paths.main_config_path)

    yield config_parser

    with open(app_data_paths.main_config_path, 'w+') as f:
        config_parser.write(f)
