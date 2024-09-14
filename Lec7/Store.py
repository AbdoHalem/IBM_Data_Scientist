hours = int(input("Enter number of working hours per day: "))
rate = int(input("Enter rate per one hour: "))

daily_pay = hours * rate
weekly_pay = daily_pay * 7
monthly_pay = weekly_pay * 4

print(f"Payment per day = {daily_pay}$\n", f"Payment per week = {weekly_pay}$\n",
      f"Payment per month = {monthly_pay}$", sep="")