# All the imports on top, just for the sake of convention, not mandatory
from pyrogram import Client, filters


'''===========EDITABLES==========='''

preFix = "?" # Change this character for a custom command prefix
cmds = ["mycmd", "mycmd@botusername"] # Change the command list accordingly
HELP = F"{preFix}{cmds[0]} - Short info about mycommand" # Provide brief and meaningful help information about what the command is for

'''-------------------------------'''


command = lambda cmd: filters.command(cmd, prefixes = preFix)

@Client.on_message(command(cmds))
async def FunctionName_SameAs_FileName(app, msg): # The function name will be myFunc if the file name is myFunc.py
  # Function Body