import matplotlib.pyplot as plt
import pandas as pd

material = input("0 = acrylic\n1 = aluminum\n2 = steel\n3 = nylon\n\nEnter Integer: ")

try:
    material = int(material)
except(ValueError):
    print("Incorrect input")
    quit()

if material == 0:
    name = 'Acrylic'
    token = 'Acrylic.xlsx'
    length = 12.7
    width = 2.9

elif material == 1:
    name = 'Aluminium'
    token = 'Al alloy.xlsx'
    length = 13
    width = 2.9

elif material == 2:
    name = 'Mild Steel'
    token = 'Mild steel.xlsx'
    length = 13
    width = 2.9

elif material == 3:
    name = 'Nylon'
    token = 'Nylon 6.xlsx'
    length = 12.7
    width = 1.6

else:
    print("incorrect input")
    quit()

entire_data = pd.ExcelFile(token)


for i in range(0, 3):

    data = pd.read_excel(entire_data, i)

    if "Load" in data.columns:
        load = data.get("Load")
    else:
        load = data.get("Load N")

    if "Strain" in data.columns:
        strain = data.get("Strain")
    else:
        strain = data.get("Strain %")

    stress = load[1:] / (length * width)


    plt.plot(strain[1:], stress)
    plt.ylabel("Stress MPa")
    plt.xlabel("Strain %")
    plt.title(name + " " + str(i + 1))
    plt.show()

