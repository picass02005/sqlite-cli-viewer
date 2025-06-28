import pretty_print
from CommandObjects import CommandObject, CommandConstant


class Schema(CommandObject):
    aliases = ["schema"]
    arguments = ["PATTERN"]
    help_message = "Show the CREATE statements matching PATTERN"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        if len(args := input_str.split(" ")) != 2:
            pretty_print.error("Missing parameter PATTERN" if len(args) == 1 else "Too much parameters")
            return

        cursor = cmd_const.db.execute(
            "SELECT sql FROM sqlite_schema "
            "WHERE name NOT LIKE 'sqlite_%' AND NAME LIKE ?;",
            (args[1],)
        )

        pretty_print.pretty_print_table(cursor.fetchall(), ["SQL Statement"], multiline=True)
