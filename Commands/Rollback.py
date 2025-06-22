from CommandObjects import CommandObject, CommandConstant


class Rollback(CommandObject):
    aliases = ["rollback"]
    arguments = []
    help_message = "Rollback unsaved changes since last commit\nTHIS COMMAND ONLY WORKS IN UNSAFE MODE"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        cmd_const.db.rollback()
        print("Database changes rolled back")
