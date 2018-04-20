import textwrap

from todoi_cli.synctodoist import synctodoist


class TodoistProject:
    api, config = synctodoist()

    @classmethod
    def create(cls, args):
        createdproject = cls.api.projects.add(args.project_name)
        cls.api.commit()

        message = """
        
        Created the following project
        ====================================
        {} {}
        """[1:-1].format(createdproject['id'], createdproject['name'])

        print(textwrap.dedent(message))

    @classmethod
    def archive(cls, args):
        projectid = args.project_id
        project = cls.api.projects.get_by_id(projectid)

        project.archive()
        cls.api.commit()

        message = """
        
        Archived the following project
        ====================================
        {} {}
        """[1:-1].format(projectid, project['name'])

        print(textwrap.dedent(message))
