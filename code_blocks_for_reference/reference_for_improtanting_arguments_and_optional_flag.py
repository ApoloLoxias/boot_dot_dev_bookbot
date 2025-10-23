import sys

try:
    if sys.argv[2] == "--non-alpha": print("text")
    else: print("flag not recognized")
except Exception: print("no text")


print(sys.argv[1], sys.argv[0])