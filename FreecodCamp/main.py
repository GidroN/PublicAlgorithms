# (May be FINISHED)

def arithmetic_arranger(mass, result=False):
    if len(mass) > 5:
        print("Error: Too many problems.")
        quit()
    output_mass = []
    for i in range(0, len(mass)):
        time_mass = mass[i].split()
        for j in range(0, len(time_mass)):
            if j == 1:
                if time_mass[j - 1].isdigit() and time_mass[j + 1].isdigit():
                    if len(time_mass[j + 1]) <= 4 and len(time_mass[j - 1]) <= 4:
                        if time_mass[j] == "-":
                            output_mass.append(int(time_mass[j - 1]) - int(time_mass[j + 1]))
                        elif time_mass[j] == "+":
                            output_mass.append(int(time_mass[j - 1]) + int(time_mass[j + 1]))
                        else:
                            print(f"Error: Operator must be '+' or '-'.")
                            quit()
                    else:
                        print("Error: Numbers cannot be more than four digits.")
                        quit()
                else:
                    print("Error: Numbers must only contain digits.")
                    quit()
            if len(time_mass[0]) > len(time_mass[2]):
                largest = len(time_mass[0])
            else:
                largest = len(time_mass[2])

        if result is True:
            print(f"""  {time_mass[0]}\n{time_mass[1]} {time_mass[2]}\n{('-' * largest) + '--'}\n{' ' * ((largest + 2) - len(str(output_mass[i])))}{output_mass[i]}""")
            print()
        else:
            print(f"""  {time_mass[0]}\n{time_mass[1]} {time_mass[2]}\n{('-' * largest) + '--'}""", end='   ')
            print()


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

