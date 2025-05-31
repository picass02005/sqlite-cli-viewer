import sqlite3

import pretty_print

class Commands:
    def __init__(self, db: sqlite3.Connection):
        self.db = db


    def tables(self, input_str: str) -> None:
        if len(args := input_str.split(" ")) > 1:
            arg = f"{args[1]}"

        else:
            arg = "%"

        cursor = self.db.execute(
            "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND NAME LIKE ?;",
            (arg,)
        )

        print(cursor.fetchall())
        print("TODO: pretty print")


    def commit(self) -> None:
        self.db.commit()
        self.need_commit = False
        print("Change wrote to database\n"
              "Note: if you're using safe mode, your changes will be copied into database when you close it")


    def rollback(self) -> None:
        self.db.rollback()
        self.need_commit = False
        print("Database changes rolled back")


    def process_command(self, input_str: str):
        match input_str.lower():
            case ".tables" | ".table":
                self.tables(input_str)

            case ".commit":
                self.commit()

            case ".rollback":
                self.rollback()

            case _:
                try:
                    # Executing SQL command
                    print(self.db.execute(input_str).fetchall())

                except Exception as err:
                    pretty_print.error(f"{type(err)}: {err}")
                print("TODO")
