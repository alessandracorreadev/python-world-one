name = input("Studant name: ").strip().title()
average = float(input("Average: "))

if average >= 7:
    situation = "approved"
elif 5 <= average < 7:
    situation = "recovery"
else:
    situation = "failed"

student_data = {'name': name,
                'average': average,
                'situation': situation
                }

print('-'*30)
for key, value in student_data.items():
    print(f"{key.capitalize()} is {value}.")
