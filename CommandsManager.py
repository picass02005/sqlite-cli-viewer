import sqlite3
from argparse import Namespace
from typing import List

import pretty_print
from CommandObjects import CommandObject, CommandConstant
from Commands.Clear import Clear
from Commands.Commit import Commit
from Commands.Help import Help
from Commands.Quit import Quit
from Commands.Rollback import Rollback
from Commands.Tables import Tables


class CommandsManager:
    COMMAND_PREFIX: str = "."
    COMMAND_CLASSES: List[CommandObject] = [Clear, Commit, Quit, Rollback, Tables, Help]

    def __init__(self, db: sqlite3.Connection, cli_args: Namespace):
        self.db = db

        self.cmd_const = CommandConstant(db, cli_args)

    def process_command(self, input_str: str):
        if input_str.startswith(self.COMMAND_PREFIX):
            cmd = input_str.split(" ")[0].lower()
            executed: bool = False
            for i in self.COMMAND_CLASSES:
                for j in i.aliases:
                    if cmd == f"{self.COMMAND_PREFIX}{j}":
                        i.callback(self.cmd_const, input_str)
                        executed = True
                        break  # Used to avoid iterating over other commands

            if not executed:
                pretty_print.error(
                    f"Unknown command. You can type {self.COMMAND_PREFIX}help to get a list of available commands"
                )

        else:
            try:
                # Executing SQL command
                v = self.db.execute(input_str).fetchall()

                col_name = None

                if input_str.lower().startswith("select"):
                    if (s := input_str.split(" "))[1] == "*":
                        try:
                            col_name = [i[1] for i in self.db.execute(f"PRAGMA table_info('{s[3]}')").fetchall()]

                        except sqlite3.OperationalError:
                            pass

                    else:
                        col_name = []
                        s.pop(0)
                        while s:
                            if s[0].lower() == "from":
                                s = []

                            else:
                                col_name.append(s.pop(0).split(",")[0])

                pretty_print.pretty_print_table(
                    v,
                    col_name
                )

            except Exception as err:
                pretty_print.error(f"{type(err)}: {err}")

# TODO: .multiline
