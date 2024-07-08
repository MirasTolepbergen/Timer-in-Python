from datetime import datetime

user_input = input("please enter a task with a deadline in the format: task:dd.mm.yy\n")
input_list = user_input.split(":")

task = input_list[0]
deadline = input_list[1]
print(input_list)

deadline_date = datetime.strptime(deadline, "%d.%m.%y")
today_date = datetime.today()
time_till = deadline_date - today_date

print(f"Tme remaining: {task} --> {time_till.days} days")