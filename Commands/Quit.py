import argparse
import sqlite3

import db_management
import pretty_print
from CommandObjects import CommandObject, CommandConstant


class Quit(CommandObject):
    aliases = ["quit", "q"]
    arguments = []
    help_message = "Quit this interpreter. If opened in safe mode, will ask if you want to save"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        on = cmd_const.cli_args.database != ":memory:"
        commit: bool = False
        while on:
            match input("Would you like to save your changes? (y/n)\n>>> ").lower():
                case "yes" | "y":
                    commit = True
                    on = False

                case "no" | "n":
                    on = False

        if cmd_const.cli_args.unsafe:
            if commit:
                cmd_const.db.commit()

            else:
                cmd_const.db.rollback()

            db_management.unsafe_close(cmd_const.db)

        else:
            if commit:
                db_management.safe_close(cmd_const.db, cmd_const.cli_args.database)

            else:
                cmd_const.db.close()

        pretty_print.info("Database closed")
        exit(0)
