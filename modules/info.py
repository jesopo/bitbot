import os
from src import IRCBot, ModuleManager, utils

class Module(ModuleManager.BaseModule):
    @utils.hook("received.command.version")
    def version(self, event):
        commit = utils.git_commit(self.bot.directory)

        out = "Version: BitBot %s" % IRCBot.VERSION
        if not commit == None:
            branch, commit = commit
            out = "%s (%s@%s)" % (out, branch or "", commit)
        event["stdout"].write(out)

    @utils.hook("received.command.source")
    def source(self, event):
        event["stdout"].write("Source: %s" % IRCBot.SOURCE)
