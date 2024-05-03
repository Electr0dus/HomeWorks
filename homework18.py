class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1


area_buiding = []
for i in range(40):
    my_buiding = Buiding()
    area_buiding.append(my_buiding)

print(area_buiding)
print(Buiding.total)