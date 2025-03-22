task = input("enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input("is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        priority_text = "high priority"
    case "medium":
        priority_text = "medium priority"
    case "low":
        priority_text = "low priority"
    case _: 
        priority_text = "unknown priority"
        
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} task that requires immediate attention today!")
else:
    print(f"Reminder: '{task}' is a {priority_text} task. Consider completing it when you have free time.")

