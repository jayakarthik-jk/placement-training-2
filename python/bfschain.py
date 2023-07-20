class Member:
    def __init__(self, parent_name, children: list):
        self.name = parent_name
        self.children = children

    def print(parent, intent = ""):
        commision = 250 if len(parent.children) == 0 else len(parent.children) * 500
        print(f"{intent}├──{parent.name}:{commision}")
        for child in parent.children:
            Member.print(child, intent=f"{intent}    ")

def get_nodes(parent_name):
    root = Member(parent_name, [])
    queue: list[Member] = [ root ]
    while len(queue) != 0:
        current = queue.pop(0)
        child_existence = input(f"does {current.name} has childrens (yes / no): ")
        if child_existence.lower().startswith("y"):
            children = input(f"Enter the {current.name}'s children names: ")
            children = children.split(" ")
            for child in children:
                child = Member(child, [])
                current.children.append(child)
                queue.append(child)
        else:
            current.children = [  ]
    return root

parent_name = input("Enter the parent name: ")
parent = get_nodes(parent_name)
print("Commision details:")
Member.print(parent)