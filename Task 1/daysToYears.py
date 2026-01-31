days=int(input("Enter Days: "))
years=days//365
remaining_days=days%365
weeks=remaining_days//7
remaining_days %=7
print(f"{days} Equal to {years} Years {weeks} Weeks {remaining_days} Days")