import pretty_print
from CommandObjects import CommandObject, CommandConstant


class Commit(CommandObject):
    aliases = ["commit"]
    arguments = []
    help_message = "Commit unsaved changes into DB\nTHIS COMMAND ONLY WORKS IN UNSAFE MODE"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        cmd_const.db.commit()
        print("Change wrote to database")
        pretty_print.info("If you're using safe mode, your changes will be copied into database when you close it")
