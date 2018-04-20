import json
import requests
import textwrap

from datetime import datetime
from todoi_cli.synctodoist import synctodoist


def gettogglprojectid(token, project_name):

    url = 'https://www.toggl.com/api/v8/me?with_related_data=true'

    get_result = requests.get(url, auth=token).json()
    togglproject = get_result['data']['projects']

    for pj in togglproject:

        if pj['name'] == project_name:
            togglprojectid = pj['id']
            return togglprojectid

    return None

class Toggl:

    api, config = synctodoist()
    headers = {'content-type': 'application/json'}
    toggltoken = config[0]['API_KEY']['toggl']
    toggltimeformat = config[0]['TIME_FORMAT']['toggl']

    @classmethod
    def start(cls, args):
        token = (cls.toggltoken, 'api_token')
        todo_item = cls.api.items.get_by_id(args.task_id)
        item_name = todo_item['content']
        label_ids = todo_item['labels']
        project_id = todo_item['project_id']

        project_name = cls.api.projects.get_by_id(project_id)['name']
        togglprojectid = gettogglprojectid(token, project_name)

        label_names = []

        for label_id in label_ids:
            label = cls.api.labels.get_by_id(label_id)
            label_names.append(label['name'])

        start_time = datetime.now().strftime(cls.toggltimeformat)

        postdata = {'time_entry': {'description': item_name, 'pid': togglprojectid, 'tags': label_names,
                                   'duration': 12000, 'start': start_time, 'created_with': "curl"}}

        postresult = requests.post('https://www.toggl.com/api/v8/time_entries/start',
                                   auth=token, data=json.dumps(postdata), headers=cls.headers)

        if postresult.status_code != 200:
            print('error: {}'.format(postresult.text))
            return

        message = """
        
        Time tracking start
        =============================
        {} {}
        """[1:-1].format(args.task_id, item_name)

        print(textwrap.dedent(message))

    @classmethod
    def stop(cls, args):
        token = (cls.toggltoken, 'api_token')

        run_time_entry = requests.get('https://www.toggl.com/api/v8/time_entries/current', auth=token).json()
        run_time_entry_id = run_time_entry['data']['id']

        stop_url = 'https://www.toggl.com/api/v8/time_entries/{time_entry_id}/stop'.format(
            time_entry_id=run_time_entry_id)

        putresult = requests.put(stop_url, auth=token, headers=cls.headers)

        if putresult.status_code != 200:
            print('error: {}'.format(putresult.text))
            return

        message = """
        
        Stop time tracking
        -------------------------
        {} {}
        """[1:-1].format(run_time_entry_id, run_time_entry['data']['description'])

        print(textwrap.dedent(message))
