#Mad libs 

print("Welcome to my Mad Libs game!")

name = input("Enter a name: ")
adjective1 = input("Enter an adjective (e.g. happy, tall, green): ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
noun1 = input("Enter a noun (e.g. book, car, tree): ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")

story = f"One day, {name} was walking through the forest when they came across a {adjective1} {noun1}. " \
        f"They were surprised to see a {adjective2} {animal} sitting on top of it. " \
        f"The {animal} was eating a {food} and looked very {adjective3}. " \
        f"{name} decided to take a picture with the {animal} and the {noun1}. " \
        f"After that, they continued their journey and found a {noun2} hidden behind a tree."

print("\nHere is your Mad Libs story:")
print(story)




#1. User se kuch words input liye jate hain (name, adjective, noun, animal, food).
#2. In words ka use karke ek kahani banai jati hai.
#3. Kahani user ko dikhai jati hai.
