# superscript generator
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


# Formula to calculate BMI : weight / (height ** 2)
def choices():
    print("=" * 55)
    print("\t\t\t\tBMI ( Body Mass Indicator )")
    print("=" * 55)
    print("1. kg / cm\t\t3. kg / m")
    print("2. lbs / cm\t\t4. lbs / m")
    print("=" * 55)


def option():
    print("=" * 55)
    print("\t\t\t\t\t\tOPTION")
    print("=" * 55)
    print("1. Show my convertion history")
    print("2. Continue to my convertion")
    print("0. Exit this program :(")


def condition():
    if (calculate < 18.5):
        print("OH NO! You're UNDERWEIGHT.")
        print("You must increase your weight about ", end="")
        if inpChoices == 1:
            range = ((height / 100)**2) * (18.49 - (weight / ((height / 100)**2)))
            print(round(range, 2), "KG to make your BMI Normal (18.5 KG/M²) !\n")
        elif inpChoices == 2:
            range = ((height / 100)**2) * (18.49 - ((weight * 0.45) / ((height / 100)**2)))
            print(round(range, 2), "KG to make your BMI Normal (18.5 KG/M²) !\n")
        elif inpChoices == 3:
            range = (height**2) * (18.49 - (weight / (height**2)))
            print(round(range, 2), "KG to make your BMI Normal (18.5 KG/M²) !\n")
        elif inpChoices == 4:
            range = (height**2) * (18.49 - ((weight * 0.45) / (height**2)))
            print(round(range, 2), "KG to make your BMI Normal (18.5 KG/M²) !\n")
        status = "Underweight"
        listStatus.append(status)

    elif calculate >= 18 and calculate < 25:
        print("Normal")
        print("Keep up your healthy lifestyle!")
        status = "Normal"
        listStatus.append(status)

    elif calculate >= 25 and calculate < 30:
        print("OH NO! You're OVERWEIGHT.")
        print("You must decrease your weight about ", end="")
        if inpChoices == 1:
            range = ((height / 100)**2) * ((weight / ((height / 100)**2)) - 25)
            print(round(range, 2), "KG to make your BMI Normal (<25 KG/M²) !\n")
        elif inpChoices == 2:
            range = ((height / 100)**2) * (((weight * 0.45) / ((height / 100)**2)) - 25)
            print(round(range, 2), "KG to make your BMI Normal (<25 KG/M²) !\n")
        elif inpChoices == 3:
            range = (height**2) * ((weight / (height**2)) - 25)
            print(round(range, 2), "KG to make your BMI Normal (<25 KG/M²) !\n")
        elif inpChoices == 4:
            range = (height**2) * (((weight * 0.45) / (height**2)) - 25)
            print(round(range, 2), "KG to make your BMI Normal (<25 KG/M²) !\n")
        status = "Overweight"
        listStatus.append(status)

    else:
        print("Obesity?")
        print('')
        status = "Obesity"
        listStatus.append(status)


choices()
inpChoices = int(input("What measurement do you prefer? (Height / Weight) ?? "))

isCondition = True
listWeight = []
listHeight = []
listCalculate = []
listStatus = []

while isCondition:
    if inpChoices == 1:
        print("\n! You are using the (KG/ CM) Measurement !")
        print("=" * 55)

        weight = float(input("Input your weight [kg]: "))
        height = float(input("Input your height [cm]: "))
        calculate = weight / ((height / 100)**2)

        listWeight.append(str(weight))
        listHeight.append(str(height))
        listCalculate.append(str(round(calculate, 2)))

        print("-" * 55)
        print("Your BMI is", round(calculate, 2), "Kg/M", end="")
        print(get_super("2"), end=" ")
        condition()

    elif inpChoices == 2:
        print("\n! You are using the (LBS/ CM) Measurement !")
        print("=" * 55)
        
        weight = float(input("Input your weight [LBS]: "))
        height = float(input("Input your height [CM]: "))
        calculate = (weight * 0.45) / ((height / 100)**2)

        listWeight.append(str(weight))
        listHeight.append(str(height))
        listCalculate.append(str(round(calculate, 2)))

        print("-" * 55)
        print("Your BMI is", round(calculate, 2), "Kg/M", end="")
        print(get_super("2"))
        condition()

    elif inpChoices == 3:
        print("\n! You are using the (KG/ M) Measurement !")
        print("=" * 55)

        weight = float(input("Input your weight [kg]: "))
        height = float(input("Input your height [M]: "))
        calculate = weight / (height**2)

        listWeight.append(str(weight))
        listHeight.append(str(height))
        listCalculate.append(str(round(calculate, 2)))

        print("-" * 55)
        print("Your BMI is", round(calculate, 2), "Kg/M", end="")
        print(get_super("2"))
        condition()

    elif inpChoices == 4:
        print("\n! You are using the (LBS/ M) Measurement !")
        print("=" * 55)

        weight = float(input("Input your weight [lbs]: "))
        height = float(input("Input your height [m]: "))
        calculate = (weight * 0.45) / (height**2)

        listWeight.append(str(weight))
        listHeight.append(str(height))
        listCalculate.append(str(round(calculate, 2)))

        print("-" * 55)
        print("Your BMI is", round(calculate, 2), "Kg/M", end="")
        print(get_super("2"))
        condition()

    print("=" * 55)
    again = input("Do you wish to calculate another BMI (yes/no) : ")
    if again == "yes":
        continue
    elif again == "no":
        option()
        inpOption = int(input("Your choice : "))
        while inpOption != 0 and inpOption != 2:
            if inpOption == 1:
                i = 1
                for x in range(len(listWeight)):
                    print(i, "#")
                    print("=" * 18)
                    print("Weight : ", listWeight[x])
                    print("Height : ", listHeight[x])
                    print("BMI    : ", listCalculate[x])
                    print("Status : ", listStatus[x])
                    print("=" * 18)
                    print()
                    i += 1
                option()
                inpOption = int(input("Your choice : "))
        if (inpOption == 2):
            continue
        else:
            isCondition = False
