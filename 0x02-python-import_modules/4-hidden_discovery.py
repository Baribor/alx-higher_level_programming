#!/usr/bin/python3

if __name__ == "__main__":
    hiddens = __import__("hidden_4")
    for name in dir(hiddens):
        if not name.startswith("__"):
            print(name)
