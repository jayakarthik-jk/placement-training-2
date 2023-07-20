i_walls = []
e_walls = []
for i in range(int(input("Enter the number of interior walls: "))):
    i_walls.append(float(input(f"Enter interior wall {i + 1} surface area: ")) * 18)

for i in range(int(input("Enter the number of exterior walls: "))):
    e_walls.append(float(input(f"Enter exterior wall {i + 1} surface area: ")) * 12)

print(f"Total: {sum(i_walls) + sum(e_walls)}")