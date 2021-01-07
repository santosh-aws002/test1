# BMI = (wgt in kgs / height in mt sq)
#BMI * 703 (imperail version)

def gather_info():
    height = float(input("What's your height ? (inches or meters) : "))
    weight = float(input("what's your weight ? (pounds or kilograms) : "))
    system = input("Are your measurement's in metric or imperail units ? : ").lower().strip()
    return (height, weight, system)

def cal_bmi(weight, height, system='metric'):
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = cal_bmi(weight, height, system)
        print(f"your bmi is {bmi}")
        break
    elif system.startswith('m'):
        bmi = cal_bmi(weight, height)
        print(f"your bmi is {bmi}")
        break
    else:
        print(" Error: unknown measurement system. Please use imperail")



