import board
import os

uname = os.uname()
print(f"Machine: {uname.machine}")
print(f"Nodename: {uname.nodename}")
print(f"Sysname: {uname.sysname}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"BoardID: {board.board_id}")
print("This board offer the following features:")
for feature in dir(board):
    print(feature)