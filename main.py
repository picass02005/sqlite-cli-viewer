import argparse

import db_management
import pretty_print
from CommandsManager import CommandsManager

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Open a sqlite database and show a prompt\n"
                    "By default, the opened database is copied in memory to avoid changing it",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "database",
        nargs="?",
        help="File path to the database to open\n"
             "To open a memory database, you can specify :memory:"
    )
    parser.add_argument(
        "--unsafe",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Open the database in unsafe mode\n"
             "When this is used, changes are directly made on your database file\n"
             "By default, your database is copied in memory and only get pushed into your database when closing it"
    )

    args = parser.parse_args()

    if args.database is None:
        parser.print_help()
        exit(0)

    if args.unsafe:
        db = db_management.unsafe_open(args.database)

    else:
        db = db_management.safe_open(args.database)

    cmd = CommandsManager(db, args)

    while True:  # Quit will stop this loop by raising an exit(0)
        input_str = input(">>> ").strip()

        cmd.process_command(input_str)
