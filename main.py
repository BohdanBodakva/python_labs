from binary_tree import Tree, Node

if __name__ == "__main__":
    tree = Tree()

    tree.insert_into_tree(Node("voltmeter", "ty-8", 20, 1999))
    tree.insert_into_tree(Node("ammeter", "asd-17", 16, 2016))
    tree.insert_into_tree(Node("optocoupler", "tron", 32, 2010))
    tree.insert_into_tree(Node("dynamometer", "sam-177", 11, 1999))
    tree.insert_into_tree(Node("manometer", "b-4", 9, 1999))
    tree.insert_into_tree(Node("hygrometer", "g-01", 104, 2010))
    tree.insert_into_tree(Node("ohmmeter", "q8", 104, 2010))

    tree.print_tree()
    print("=======================================================================================")
    tree.remove_nodes_with_year(1999)
    tree.print_tree()

