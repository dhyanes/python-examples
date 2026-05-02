def calculate_percentage(**marks):
    print("\nSubjects entered:")
    
    for subject in marks:
        print(subject)
    
    return sum(marks.values()) / len(marks)

subjects = {}
n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input(f"Enter subject {i+1} name: ")
    mark = float(input(f"Enter marks for {name}: "))
    subjects[name] = mark

result = calculate_percentage(**subjects)
print("Percentage:", result)