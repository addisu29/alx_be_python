# Ask user for a single task
task = input("Enter your task: ").strip()

# Ask for task priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"

# Modify message if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = f"Note: {message}. Consider completing it when you have free time."

# Print the customized reminder
print(f"Reminder: {message}" if time_bound == "yes" else message))
