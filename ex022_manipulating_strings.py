name = input("Enter your full name: ").strip()
split_name = name.split()
join_name = ''.join(split_name)

print(f"Uppercased name: {name.upper()}")
print(f"Lowercased name: {name.lower()}")
print(f"Your name has {len(join_name)} letters.")
print(f"Your first name has {len(split_name[0])} letters.")
