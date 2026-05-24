#Capture information of 2 users. This information includes their name, age and height (in cm).
#Display each user&amp;#039;s information in a sentence format.
#Then calculate and display the total combined height of both users.

#User 1 information
user1=input('Enter your name:')
user1=str(user1)
user1_age=input("Enter your age: ")
user1_age=int(user1_age)
user1_height=input('Enter your height in cm: ')
user1_height=int(user1_height)


#User 2 information
user2=input('Enter your name:')
user1=str(user1)
user2_age=input("Enter your age: ")
user2_age=int(user2_age)
user2_height=input('Enter your height in cm: ')
user2_height=int(user2_height)



#Calculate combined height
combined_height=user1_height+user2_height

print(f'{user1} is {user1_age} years old and {user1_height} centimeters tall' )
print(f'{user2} is {user2_age} years old and {user2_height} centimeters tall' )
print(f'{user1} and {user2}s combined height is {combined_height} centimeters')



