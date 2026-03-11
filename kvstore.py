
import os

DB_FILE = "data.db"

class KVStore:
    def __init__(self):
        self.store = []
        self.load()

     def load(self):
       if not os.path.exists(DB_FILE):
            open(DB_FILE, "a").close()

        with open(DB_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" ", 2)
                if parts[0] == "SET":
                    self.set(parts[1], parts[2], persist=False)

    def find_key(self, key):
        for i in range(len(self.store)):
            if self.store[i][0] == key:
                return i
        return -1


    def set(self, key, value, persist=True):
        index = self.find_key(key)

        if index == -1:
            self.store.append([key, value])
        else:
            self.store[index][1] = value

        if persist:
            with open(DB_FILE, "a") as f:
                f.write(f"SET {key} {value}\n")

        print("OK")

    def get(self, key):
        index = self.find_key(key)

        if index == -1:
            print()
        else:
            print(self.store[index][1])


def main():
    kv = KVStore()

    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        parts = command.split(" ", 2)

        if parts[0] == "SET" and len(parts) == 3:
            kv.set(parts[1], parts[2])

        elif parts[0] == "GET" and len(parts) == 2:
            kv.get(parts[1])

        elif parts[0] == "EXIT":
            break

        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
