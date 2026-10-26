name = input("Your name: ")
experience_years = float(input("Python experience in years (e.g. 0.5): "))
weekly_goal_hours = int(input("Weekly learning goal (hours): "))
study_days = int(input("Planned study days per week: "))
used_git = input("Have you used Git before? (yes/no): ").strip().lower() == "yes"

if study_days <= 0:
    study_days = 1

hours_per_day = weekly_goal_hours / study_days

print("\n===== Intern Profile =====")
print(f"Name: {name}")
print(f"Python experience: {experience_years} years")
print(f"Weekly goal: {weekly_goal_hours} hours")
print(f"Study days per week: {study_days}")
print(f"Used Git before: {used_git}")
print(f"Planned hours per study day: {hours_per_day:.2f}")