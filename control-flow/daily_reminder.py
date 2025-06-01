task = input("input a task description : ")
time_bound = input("task is time-bound (yes or no): ")
priority = input(" task’s priority (high, medium, low): ")

match priority:
    case "high":
        message = f"'{task}' is a {priority} priority task"
    case "medium":
        message = f"'{task}' is a {priority} priority task"
    case "low":
        message = f"'{task}' is a {priority} priority task"
    case _:
        message = f"'{task}' is an unknown priority task"

if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += ". Consider completing it when you have free time."

# Final reminder
print("\n📌 Reminder:")
print(message)