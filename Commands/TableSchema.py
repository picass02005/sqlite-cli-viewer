import pretty_print
from CommandObjects import CommandObject, CommandConstant


class TableSchema(CommandObject):
    aliases = ["table_schema", "t_schema"]
    arguments = ["TABLE"]
    help_message = "Show the TABLE schema"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        if len(args := input_str.split(" ")) != 2:
            pretty_print.error("Missing parameter TABLE" if len(args) == 1 else "Too much parameters")
            return

        cursor = cmd_const.db.execute(f"pragma table_info(\"{args[1]}\");")
        content = cursor.fetchall()

        if content:
            pretty_print.pretty_print_table(
                content,
                ["Column ID", "Name", "Type", "Not null", "Default value", "Primary key"],
                multiline=True,
                show_number_entries=False
            )

        else:
            print(f"Table {args[1]} not found")
