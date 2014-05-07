--- ../kippo/commands/base.py
+++ ../kippo/commands/base.py
@@ -48,5 +48,5 @@
             self.honeypot.terminal.loseConnection()
         else:
             self.writeln('bash: exxxit: command not found')
-commands['exxxit'] = command_exxxit
+#commands['exxxit'] = command_exxxit
