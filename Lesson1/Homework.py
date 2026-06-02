#Capture information of 2 users. This information includes their name, age and height (in meters).
#Display each user&amp;#039;s information in a sentence format.
#Then calculate and display the total combined height of both users.



def add_total_height(users):
    total = 0
    for user in users:
        total += user["Height"]
    return total
userinfo = []

for i in range(2):
    print(f"\nCapture information for User {i + 1}:")

    name = input("Enter name: ")
    height = float(input("Enter height in meters (e.g., 1.75): "))
    age = int(input("Enter age: "))

    user_info = {
        "Name": name,
        "Height": height,
        "Age": age
    }

    userinfo.append(user_info)

# Add the heights
total_height = add_total_height(userinfo)

print("\nUser Details:")
for n, user in enumerate(userinfo, start=1):
    print(f"User {n}: {user}")

print(f"\nHeight of two users is : {total_height:.2f} meters")









