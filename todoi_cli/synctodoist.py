import sys
import textwrap

from todoi_cli.auth import auth
from todoi_cli.checkconfig import checkconfig
from todoist.api import TodoistAPI


def synctodoist():
    config = checkconfig()
    api_key = config[0]['API_KEY']['todoist']

    if api_key is '':
        # message = """
        # Authentication of todoist is not done yet.
        # Please execute "python main.py auth todoist" command first.
        # """[1:-1]
        #
        # print(textwrap.dedent(message))

        auth()
        sys.exit(1)

    api = TodoistAPI(api_key)
    api.sync()

    return api, config
