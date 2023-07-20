class Member:
    def __init__(self, parent_name, children: list):
        self.name = parent_name
        self.children = children

    def print(parent, intent = ""):
        commision = 250 if len(parent.children) == 0 else len(parent.children) * 500
        print(f"{intent}{parent.name}:{commision}")
        for child in parent.children:
            Member.print(child, intent=f"{intent}    ")

def get_nodes(parent_name):
    child_existence = input(f"does {parent_name} has childrens (yes / no): ")
    if child_existence.lower().startswith("y"):
        children = input(f"Enter the {parent_name}'s children names: ")
        children = children.split(" ")
        for (i, child) in enumerate(children):    
            children[i] = get_nodes(child)
        return Member(parent_name, children)
    else:
        return Member(parent_name, [])
    
parent_name = input("Enter the parent name: ")
parent = get_nodes(parent_name)
print("Commision details:")
Member.print(parent)