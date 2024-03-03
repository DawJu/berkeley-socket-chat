*The code was written using Python 2.7 and its libraries `socket` and `threading`, on Linux.*

To use the chat, open the terminal and navigate to the directory that has the `Chat.py` file. Run the file by entering `python2 Chat.py`. It will create a multi-thread TCP server, accepting up to 5 simultaneous connections.

To connect to the server, you need to open a new terminal window and use `nc localhost 9999`. Then choose the nickname that you want to use in chat. A message will show in chat that a new user has joined.
To add another user, open another terminal window and repeat the previous step. Now users can send messages that will appear in the first terminal.

Leaving the chat by closing the terminal or using `ctrl+C` will send a message that the user has left.
