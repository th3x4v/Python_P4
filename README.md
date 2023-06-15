# Chess Tournament Management Application

### Openclassroom Project 04

This project consists of creating an application that allows the creation of the structure of a chess tournament and the addition of players to a database. The program uses an algorithm to calculate the rotation of players so that the matches are fair and do not repeat (Swiss tournament algorithm).

The program uses the MVC (Models - Views - Controllers) design pattern and uses the TinyDB library to save players and tournaments.

It allows you to:

- Create and save players.
- Create and save tournaments.
- Launch tournaments.
- Stop a tournament in progress and resume later.



## Prerequisites

You must install Python, the latest version can be found here
https://www.python.org/downloads/

Python scripts run from a terminal, to open a terminal on Windows, press ```windows key + r``` and type ```cmd```.

On Mac, press ```command key + space``` and type ```terminal```.

In Linux, you can open a terminal by pressing the keys ```Ctrl + Alt + T```.

The program uses several external libraries and Python modules, which are listed in the ```requirements.txt``` file

You can install an external environment via the command 
```bash
pip install venv
```
Activate the environment via the command:
- On Mac and Linux, 
```bash
source venv/bin/activate
```
- On Windows,
```bash
venv\Scripts\activate.bat
```

in the terminal, then enter the command:

```bash
pip install -r requirement.txt
```
in order to install all the libraries.



## Starting the program

The program is written in Python, copy all the files and directories from the repository, and launch the program from a terminal using the command:

```bash
python -m chess
```



## Flake8 report

The repository contains a flake8 report, which shows no errors. It is possible to generate a new one by installing the ```flake8``` module and entering in the terminal:

```bash
flake8 /chess
```

The ```.flake8``` file at the root contains the parameters regarding the report generation.

The report is located in the ```flake-report``` directory.