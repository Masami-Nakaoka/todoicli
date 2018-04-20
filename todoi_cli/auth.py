import requests
import sys

from todoi_cli.checkconfig import checkconfig
from getpass import getpass


def auth(args=None):
    if args is None:
        auth_target = 'todoist'
    else:
        auth_target = args.target
    
    config_check_result = checkconfig()
    config = config_check_result[0]
    config_path = config_check_result[1]
    api_key = config['API_KEY'].get(auth_target)
    
    if api_key == '':
        if auth_target == 'todoist':
            api_key = None
            roop_count = 0
            while api_key is '' and roop_count <= 4:
                api_key = input('Please enter api key of todoist: ')
                roop_count += 1
                
                if api_key is '' and roop_count == 4:
                    print('Feild todoist authentication')
                    sys.exit(1)
                    
                

        elif auth_target == 'toggl':
            toggl_id = input('Enter e-mail: ')
            toggl_pass = getpass('Enter password: ')

            payload = (toggl_id, toggl_pass)

            res = requests.get('https://www.toggl.com/api/v8/me', auth=payload).json()

            api_key = res['data']['api_token']
            
        config['API_KEY'][auth_target] = api_key
        with open(str(config_path), 'w') as f:
            config.write(f)

        print('Authentication is completed')

    else:
        print('{} has already been authenticated'.format(auth_target))
