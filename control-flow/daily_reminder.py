task = input("enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input("is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        reminder = f" '{task}' is a high priority task"
    case "medium":
        reminder = f" '{task}' is a medium priority task"
    case "low":
        reminder = f" '{task}' is a low priority task"
    case _: 
        reminder = f" '{task}' has an unknown priority level"
        
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
print(reminder)

