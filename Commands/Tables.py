import argparse
import sqlite3

import pretty_print
from CommandObjects import CommandObject, CommandConstant


class Tables(CommandObject):
    aliases = ["tables", "table"]
    arguments = ["?TABLE?"]
    help_message = "List names of tables matching LIKE pattern TABLE"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        if len(args := input_str.split(" ")) > 1:
            arg = f"{args[1]}"

        else:
            arg = "%"

        cursor = cmd_const.db.execute(
            "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND NAME LIKE ?;",
            (arg,)
        )

        pretty_print.pretty_print_table(cursor.fetchall(), ["Table name"])
