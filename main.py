from real_workers import Manager, Scientist, Worker, Foreman

if __name__ == "__main__":
    manager = Manager("Olexander", 27, "SoftServe")
    scientist = Scientist("Roman", 40, "Lviv Polytechnic University")
    worker = Worker("Oleh", 24, "Paper Factory")
    foreman = Foreman("Denys", 52, "Postal Warehouse")

    manager.do_work()
    scientist.do_work()
    print(worker)
    print(foreman)
    