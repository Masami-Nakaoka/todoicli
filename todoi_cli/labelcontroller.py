import textwrap

from todoi_cli.synctodoist import synctodoist


class TodoistLabel:
    api = synctodoist()[0]

    @classmethod
    def create(cls, args):
        labelname = args.label_name
        createdlabel = cls.api.labels.add(labelname)
        cls.api.commit()

        message = """
        
        Created the following label
        ====================================
        {} {}
        """[1:-1].format(createdlabel['id'], createdlabel['name'])

        print(textwrap.dedent(message))

    @classmethod
    def delete(cls, args):
        labelid = args.label_id
        label = cls.api.labels.get_by_id(labelid)

        label.delete()
        cls.api.commit()

        print("Label deleted")