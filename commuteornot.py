hourly_rate = int(input("What is your hourly rate? Rate: "))
commute_distance = int(input("How many KM do you have to drive to work? KM: "))
commute_time = float(input("How many hours does it take to drive this distance? "))
working_days = 230
cost_per_km = 35
years_living_at_location = int(input("How many years are you planning on living at your location? Maybe because you have to pay a debt. Years: "))
commuting_cost_daily = ((commute_distance*cost_per_km)+(commute_time*hourly_rate)*2)
commuting_cost_yearly = commuting_cost_daily*working_days
print(commuting_cost_yearly)

