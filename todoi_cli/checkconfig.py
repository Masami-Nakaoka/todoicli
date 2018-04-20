from configparser import ConfigParser
from pathlib import Path


def checkconfig():
    config = ConfigParser()
    config_path = Path(__file__).parent.parent.joinpath('config.ini')
    config_existence_flag = config_path.exists()

    if not config_existence_flag:
        config['API_KEY'] = {'todoist': '', 'toggl': ''}
        config['TIME_FORMAT'] = {
            'todoist': '%%a %%d %%b %%Y %%H:%%M:%%S +0000',
            'toggl': '%%Y-%%m-%%dT%%H:%%M:%%S.000Z'
        }

        with Path(config_path).open(mode='w') as f:
            config.write(f)

    config.read(str(config_path))

    return config, config_path
