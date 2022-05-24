from real_workers import Manager, Scientist, Worker, Foreman


def main():
    manager = Manager("Olexander", 27, "SoftServe")
    scientist = Scientist("Roman", 40, "Lviv Polytechnic University")
    worker = Worker("Oleh", 24, "Paper Factory")
    foreman = Foreman("Denys", 52, "Postal Warehouse")

    manager.do_work()
    scientist.do_work()
    worker.do_work()
    foreman.do_work()
    print()
    print(manager)
    print(scientist)
    print(worker)
    print(foreman)


if __name__ == "__main__":
    main()
