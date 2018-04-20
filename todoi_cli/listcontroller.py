import textwrap

from datetime import datetime, date, timedelta
from todoi_cli.synctodoist import synctodoist


class TodoistList:
    api, config = synctodoist()

    timehours = api.state['user']['tz_info']['hours']
    utctimeformat = config[0]['TIME_FORMAT']['todoist']

    
    @classmethod
    def show_all_tasks(cls, args):
        message = """
        
        All incomplete tasks list
        ====================================
        [task_id] [project_name] [due_date] [task_name]
        """[1:-1]
        print(textwrap.dedent(message))
        
        for item in cls.api.state['items']:
            if item['checked'] == 0:
                for project in cls.api.state['projects']:
                    if item['project_id'] == project['id']:
                        if item['due_date_utc'] is not None:
                            due_date = datetime.strptime(item['due_date_utc'], cls.utctimeformat) \
                                       + timedelta(hours=cls.timehours)

                        print('{} {} {} {}'.format(item['id'], project['name'], due_date, item['content']))
                    
    @classmethod
    def show_today_tasks(cls, args):
        message = """
        
        List of today's tasks and expired tasks
        ====================================
        [task_id] [project_name] [due_date] [task_name]
        """[1:-1]
        
        print(textwrap.dedent(message))

        for item in cls.api.state['items']:
            if item['due_date_utc']:
                due_date = datetime.strptime(item['due_date_utc'], cls.utctimeformat) + timedelta(hours=cls.timehours)
                if due_date.date() <= date.today() and item['checked'] == 0:
                    for project in cls.api.state['projects']:
                        if item['project_id'] == project['id']:
                            print('{} {} {} {}'.format(item['id'], project['name'], due_date, item['content']))

    @classmethod
    def show_next7days_tasks(cls, args):
        message = """

        List of 7 day tasks and expired tasks
        ====================================
        [task_id] [project_name] [due_date] [task_name]
        """[1:-1]

        print(textwrap.dedent(message))

        for item in cls.api.state['items']:
            if item['due_date_utc'] and item['checked'] == 0:
                due_date = datetime.strptime(item['due_date_utc'], cls.utctimeformat) + timedelta(hours=cls.timehours)
                sevendayslater = datetime.now() + timedelta(days=7)

                if due_date.date() <= sevendayslater.date():
                    for project in cls.api.state['projects']:
                        if item['project_id'] == project['id']:
                            print('{} {} {} {}'.format(item['id'], project['name'], due_date, item['content']))

    @classmethod
    def show_all_projects(cls, args):
        message = """
        
        All projects list
        ====================================
        [project_id] [project_name]
        """[1:-1]
        
        print(textwrap.dedent(message))
        
        for project in cls.api.state['projects']:
            if project['is_archived'] == 0 and project['is_deleted'] == 0:
                print('{} {}'.format(project['id'], project['name']))

    @classmethod
    def show_all_labels(cls, args):
        message = """
        
        All labels list
        ====================================
        [label_id] [label_name]
        """[1:-1]
        
        print(textwrap.dedent(message))
        
        for label in cls.api.state['labels']:
            if label['is_deleted'] == 0:
                print('{} {}'.format(label['id'], label['name']))
