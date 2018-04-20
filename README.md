# todoicli

## Basic Overview


todoicli is a tool for using todoist from the command line.

It has the following functions.

- Create
  - new task
  - new project
  - new label
- Delete
  -
- Display
  - all task
  - today task
  - next 7 days task
  - all project
  - all label
- Option
  - toggl
    - start/stop time tracking


## pyhton version

3.4.3

## Installation

```python
pip install todoicli
```

## After installation

Execute the following command and enter API_TOKEN of todoist.

```bash
python main.py auth todoist
```

## Usage

### Show list

- All task list

```bash
python main.py list al
```

- Today task list

```bash
python main.py list td
```

- Next 7 days task and expired task list

```bash
python main.py list n7
```

- All project list

```bash
python main.py list pj
```

- All label list

```bash
python main.py list lb
```

### Add task

```bash
python main.py add 'task_name due_date #project_name @label_name'
```

### Add project


```bash
python main.py pj create project_name
```

### Add label

```bash
python main.py lb create label_name
```

### Complete task

The repetition task has its expiration date updated, and the other tasks complete.

```bash
python main.py comp task_id
```

With the -c option, the repeat task is also completed

```bash
python main.py comp task_id -c
```

### Option

You can use the time tracking function  by entering the following command
and authenticating toggl with your email address and password.

```bash
python main.py auth toggl
```

## Command list

```bash
$ main.py --help
usage: main.py [-h] {auth,list,add,comp,del,pj,lb,toggl} ...

todoist for command line

positional arguments:
  {auth,list,add,comp,del,pj,lb,toggl}
    auth                Authentication of todoist and toggl
    list                Show task or project list
    add                 Add new task
    comp                Complete task
    del                 Delete task
    pj                  Commands that control project relationships
    lb                  Commands that control label relationships
    toggl               Initialize toggl

optional arguments:
  -h, --help            show this help message and exit

end
```

## License
- MIT