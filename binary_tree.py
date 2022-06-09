class Node:
    def __init__(self, type_of_device, brand, measurement_limit, year_of_creation):
        self.type_of_device = type_of_device
        self.brand = brand
        self.measurement_limit = measurement_limit
        self.year_of_creation = year_of_creation
        self.right = None
        self.left = None
        self.parent = None

    def __str__(self):
        return "[" + self.type_of_device + ", " + self.brand + ", " + \
               str(self.measurement_limit) + ", " + str(self.year_of_creation) + "]"

    def __repr__(self):
        return "[" + self.brand + "]"

    def __lt__(self, other):
        return self.brand < other

    def __le__(self, other):
        return self.brand <= other

    def __gt__(self, other):
        return self.brand > other

    def __ge__(self, other):
        return self.brand >= other

    def __eq__(self, other):
        return self.brand == other

    def __ne__(self, other):
        return self.brand != other


class Tree:
    def __init__(self):
        self.root = None

    def insert_into_tree(self, node):
        if self.root is None:
            self.root = node
        else:
            self.__insert_into_tree(node, self.root)

    def __insert_into_tree(self, node, current_node):
        if current_node.brand.casefold() == node.brand.casefold():
            print("Devices must have unique brands!")
        elif current_node.brand.casefold() > node.brand.casefold():
            if current_node.left is None:
                current_node.left = node
            else:
                self.__insert_into_tree(node, current_node.left)
        elif current_node.brand.casefold() < node.brand.casefold():
            if current_node.right is None:
                current_node.right = node
            else:
                self.__insert_into_tree(node, current_node.right)

    def print_tree(self):
        self.__print_tree(self.root)

    def __print_tree(self, node, level=0):
        if node is not None:
            self.__print_tree(node.right, level + 1)
            print(' ' * 5 * level + '-> ' + node.__repr__())
            self.__print_tree(node.left, level + 1)

    def print_devices_upper_measurement_line(self, measurement_line):
        self.__print_devices_upper_measurement_line(measurement_line, self.root)

    def __print_devices_upper_measurement_line(self, measurement_line, node):
        if node is not None:
            self.__print_devices_upper_measurement_line(measurement_line, node.right)
            if node.measurement_limit >= measurement_line:
                print(node)
            self.__print_devices_upper_measurement_line(measurement_line, node.left)

    def remove_nodes_with_year(self, year):
        self.__remove_nodes_with_year(self.root, year)

    def __remove_nodes_with_year(self, node, year):
        if node is not None:
            self.__remove_nodes_with_year(node.right, year)
            if node.year_of_creation == year:
                self.delete_node(node)
            self.__remove_nodes_with_year(node.left, year)

    def find_node_by_brand(self, brand):
        if self.root:
            result_node = self.__find_node_by_brand(brand, self.root)
            if result_node:
                return result_node
            else:
                return "There is no node with such brand!"
        else:
            return "Firstly you must create your tree!"

    def __find_node_by_brand(self, brand, current_node):
        if not current_node:
            return None
        elif current_node.brand == brand:
            return current_node
        elif brand < current_node.brand:
            return self.__find_node_by_brand(brand, current_node.left)
        else:
            return self.__find_node_by_brand(brand, current_node.right)

    def delete_node(self, brand):
        if self.root is None:
            print("root is None!")
            return False
        elif self.root.brand == brand:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                del_node_parent = self.root
                del_node = self.root.right
                while del_node.left:
                    del_node_parent = del_node
                    del_node = del_node.left
                self.root.brand = del_node.brand
                self.root.type_of_device = del_node.type_of_device
                self.root.measurement_limit = del_node.measurement_limit
                self.root.year_of_creation = del_node.year_of_creation
                if del_node.right:
                    if del_node_parent.brand > del_node.brand:
                        del_node_parent.left = del_node.right
                    elif del_node_parent.brand <= del_node.brand:
                        del_node_parent.right = del_node.right
                else:
                    if del_node.brand < del_node_parent.brand:
                        del_node_parent.left = None
                    else:
                        del_node_parent.right = None
            return True
        parent = None
        node = self.root
        while node and node.brand != brand:
            parent = node
            if brand < node.brand:
                node = node.left
            elif brand > node.brand:
                node = node.right
        if node is None or node.brand != brand:
            return False
        elif node.left is None and node.right is None:
            if brand < parent.brand:
                parent.left = None
            else:
                parent.right = None
            return True
        elif node.left and node.right is None:
            if brand < parent.brand:
                parent.left = node.left
            else:
                parent.right = node.left
        elif node.left is None and node.right:
            if brand < parent.brand:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            del_node_parent = node
            del_node = node.right
            while del_node.left:
                del_node_parent = del_node
                del_node = del_node.left

            node.brand = del_node.brand
            if del_node.right:
                if del_node_parent.brand > del_node.brand:
                    del_node_parent.left = del_node.right
                elif del_node_parent.brand > del_node.brand:
                    del_node_parent.right = del_node.right
            else:
                if del_node.brand < del_node_parent.brand:
                    del_node_parent.left = None
                else:
                    del_node_parent.right = None

    def delete_tree(self):
        self.__delete_tree(self.root)

    def __delete_tree(self, current_node):
        if current_node:
            self.__delete_tree(current_node.left)
            self.__delete_tree(current_node.right)
            current_node.left = None
            current_node.right = None
        self.root = None



