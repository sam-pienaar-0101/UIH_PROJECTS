# Purpose of this program is to determine fertility of human female

Patient_Name = "Jessica Nkosi"
Patient_Age = 34             # Fertility declines after 35 y/o
Patient_ID = 240028591

################# Doctors records ########################
"""
Polycystic Ovary Syndrome (PCOS):
Causes high Androgen(male hormone) and LH levels, leading to irregular or absent ovulation.
"""
Pcos_levels = 9.2
"""
Low Progesterone:
Insufficiency of this hormone after ovulation prevents the uterine lining from properly supporting...
a fertilized egg.
"""
Prog_levels = 10

Smoking = "Yes"   # Tobacco and heavy alcohol use significantly reduce fertility.
Patient_BMI = 23  # Both obesity and being underweight can cause ovulation issues.


def CheckAge(Patient_Age):
    if Patient_Age <= 30:
        print("Your age of", Patient_Age, " is good and likelihood for fertility is on average above 75%")
    elif  40 >= Patient_Age >= 31:
        print("Your age of", Patient_Age, " is moderate and likelihood for fertility is on average 66%")
    elif Patient_Age >= 41:
        print("Your age of", Patient_Age, " is not good and likelihood for fertility is on average below 50% ")
    else:
        print("Error")

print(CheckAge(Patient_Age))

def CheckMass(Patient_BMI):
    if 18.5 <= Patient_BMI <= 25:
        print("Your mass of", Patient_BMI, " is good and increases chances of fertility by 20%")
    elif 25 <= Patient_BMI <= 30:
        print("Your mass of", Patient_BMI, " is moderate and increases chances of fertility by 4%")
    elif 30 <= Patient_BMI :
        print("Your mass of", Patient_BMI, " is not good and decreases chances of fertility by 18%")
    else:
        print("Error")

print(CheckMass(Patient_BMI))

def CheckHormone(Prog_levels):
    if Prog_levels <= 3:
        print("Your progesterone levels of", Prog_levels, " is BELOW threshold and decreases chances of fertility")
    elif Prog_levels >= 3.01 :
        print("Your progesterone levels of", Prog_levels, " is MODERATE or ABOVE threshold and increases chances of fertility")
    else:
        print("Error")

print(CheckHormone(Prog_levels))






