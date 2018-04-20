#!/usr/bin/env python
import argparse

from todoi_cli.auth import auth
from todoi_cli.labelcontroller import TodoistLabel
from todoi_cli.listcontroller import TodoistList
from todoi_cli.taskcontroller import TodoistTask
from todoi_cli.togglcontroller import Toggl
from todoi_cli.projectcontroller import TodoistProject


def get_args():
    parser = argparse.ArgumentParser(
        description='todoist for command line',
        epilog='end',
        add_help=True)

    subparser = parser.add_subparsers(
        title='Subcommand list'
    )

    auth_parser = subparser.add_parser('auth', help='Authentication of todoist and toggl')
    list_parser = subparser.add_parser('list', help='Show task or project list')
    add_parser = subparser.add_parser('add', help='Add new task')
    comp_parser = subparser.add_parser('comp', help='Complete task')
    del_parser = subparser.add_parser('del', help='Delete task')
    pj_parser = subparser.add_parser('pj', help='Commands that control project relationships')
    lb_parser = subparser.add_parser('lb', help='Commands that control label relationships')
    toggl_parser = subparser.add_parser('toggl', help='Start or stop time tracking')
    
    # init parser
    auth_subparser = auth_parser.add_subparsers(title='auth')
    
    auth_todoist_parser = auth_subparser.add_parser('todoist', help='Acquire todoist authentication with API_KEY')
    auth_todoist_parser.add_argument('-tod', '--todoist', dest='target', default='todoist')
    auth_todoist_parser.set_defaults(func=auth)

    auth_toggl_parser = auth_subparser.add_parser('toggl', help='Acquire toggl authentication with API_KEY')
    auth_toggl_parser.add_argument('-tog', '--toggl', dest='target', default='toggl')
    auth_toggl_parser.set_defaults(func=auth)

    # list parser
    list_subparser = list_parser.add_subparsers()

    all_list_parser = list_subparser.add_parser('al', help='Show all incomplete tasks')
    all_list_parser.set_defaults(func=TodoistList.show_all_tasks)

    today_list_parser = list_subparser.add_parser('td', help='Show today incomplete tasks')
    today_list_parser.set_defaults(func=TodoistList.show_today_tasks)

    next7days_list_parser = list_subparser.add_parser('n7', help='Show tasks for the next 7 days')
    next7days_list_parser.set_defaults(func=TodoistList.show_next7days_tasks)

    project_list_parser = list_subparser.add_parser('pj', help='Show all projects')
    project_list_parser.set_defaults(func=TodoistList.show_all_projects)

    label_list_parser = list_subparser.add_parser('lb', help='Show all labels')
    label_list_parser.set_defaults(func=TodoistList.show_all_labels)

    # add parser
    add_parser.add_argument('taskdatastring', help='Task name', type=str, action='store')
    add_parser.set_defaults(func=TodoistTask.add)

    # comp parser
    comp_parser.add_argument('task_id', help='ID of task to be completed', type=int, action='store')
    comp_parser.add_argument('-c', '--completion', dest='completion', help='Flag to complete repeating task',
                             action='store_true', default=False)
    comp_parser.set_defaults(func=TodoistTask.complete)

    # task delete parser
    del_parser.add_argument('task_id', help='ID of the task to delete', type=int, action='store')
    del_parser.set_defaults(func=TodoistTask.delete)

    # project parser
    pj_subparser = pj_parser.add_subparsers()

    create_pj_parser = pj_subparser.add_parser('create', help='Create project')
    create_pj_parser.add_argument('project_name', help='Project_name', type=str, action='store')
    create_pj_parser.set_defaults(func=TodoistProject.create)

    archive_pj_parser = pj_subparser.add_parser('archive', help='Archive project')
    archive_pj_parser.add_argument('project_id', help='Project id', type=int, action='store')
    archive_pj_parser.set_defaults(func=TodoistProject.archive)

    # label parser
    lb_subparser = lb_parser.add_subparsers()

    create_lb_parser = lb_subparser.add_parser('create', help='Create label')
    create_lb_parser.add_argument('label_name', help='Label_name', type=str, action='store')
    create_lb_parser.set_defaults(func=TodoistLabel.create)

    del_lb_parser = lb_subparser.add_parser('del', help='Delete label')
    del_lb_parser.add_argument('label_id', help='Label id', type=int, action='store')
    del_lb_parser.set_defaults(func=TodoistLabel.delete)

    # toggl parser
    toggl_subparser = toggl_parser.add_subparsers()

    start_toggl_parser = toggl_subparser.add_parser('start', help='Start time tracking')
    start_toggl_parser.add_argument('task_id', help='Task id', type=int, action='store')
    start_toggl_parser.set_defaults(func=Toggl.start)

    stop_toggl_parser = toggl_subparser.add_parser('stop', help='Stop time tracking')
    stop_toggl_parser.set_defaults(func=Toggl.stop)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        return args
    else:
        parser.print_help()


def main():
    args = get_args()

    if args is not None:
        args.func(args)


if __name__ == '__main__':
    main()
