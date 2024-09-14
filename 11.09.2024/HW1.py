# START
runtime_minutes: int = int(input("How long is the movie in minutes?: "))
hours = runtime_minutes // 60
minutes = runtime_minutes % 60
print(f"The movie is {hours} hours and {minutes} minutes long")

# STOP
