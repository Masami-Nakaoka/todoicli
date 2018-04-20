import textwrap

from todoi_cli.synctodoist import synctodoist


class TodoistTask:
    api, config = synctodoist()
    utctimeformat = config[0]['TIME_FORMAT']['todoist']

    @classmethod
    def add(cls, args):
        taskdatastring = args.taskdatastring

        addeditem = cls.api.quick.add(taskdatastring)
        cls.api.commit()

        message = """
        
        Added new task
        ============================
        {} {} {} {}
        """[1:-1].format(addeditem['id'], addeditem['project_id'], addeditem['date_string'], addeditem['content'])

        print(textwrap.dedent(message))

    @classmethod
    def complete(cls, args):
        taskid = args.task_id
        item = cls.api.items.get_by_id(taskid)
        
        if args.completion:
            item.complete()
            
        else:
            item.close()
            
        cls.api.commit()

        message = """
        Congrats!
        You have completed the task!
        """[1:-1]

        print(textwrap.dedent(message))

    @classmethod
    def update_task(cls, args):
        pass

    @classmethod
    def uncomplete_task(cls, args):
        pass

    @classmethod
    def delete(cls, args):
        taskid = args.task_id

        item = cls.api.items.get_by_id(taskid)
        item.delete()

        cls.api.commit()

        message = """
        
        Deleted task
        =========================
        {} {} {} {}
        """[1:-1].format(item['id'], item['project_id'], item['date_string'], item['content'])

        print(textwrap.dedent(message))
