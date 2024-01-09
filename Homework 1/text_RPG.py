print("Welcome to the Chemistry Lab Adventure!")
scientist_name = input("Enter your scientist name: ")

print(f"Hello, {scientist_name}! You are a scientist in a top-secret chemistry lab.")
print("Your mission is to conduct experiments and discover a groundbreaking formula.")
print("You enter the lab and see various equipment and chemicals.")

# First choice
choice1 = input("1. Check the lab equipment\n2. Mix chemicals\nEnter your choice (1 or 2): ")

if choice1 == "1":
    # Check the lab equipment
    print(f"You, {scientist_name}, decide to inspect the lab equipment.")
    print("You find an advanced spectrophotometer and a high-speed centrifuge.")
    print("What do you want to do?")
    print("1. Use the spectrophotometer\n2. Use the centrifuge")

    # Second choice
    choice2 = input("Enter your choice (1 or 2): ")

    if choice2 == "1":
        print(f"You, {scientist_name}, use the spectrophotometer to analyze a mysterious sample.")
        print("The results reveal a unique molecular structure.")
    else:
        print(f"You, {scientist_name}, use the centrifuge to separate a mixture.")
        print("You discover a new compound in the process.")

else:
    # Mix chemicals
    print(f"You, {scientist_name}, decide to mix chemicals.")
    print("You choose two random chemicals from the shelf and mix them.")
    print("What do you want to do?")
    print("1. Analyze the reaction\n2. Dispose of the mixture")

    # Second choice
    choice2 = input("Enter your choice (1 or 2): ")

    if choice2 == "1":
        print(f"You, {scientist_name}, analyze the reaction and identify a new compound.")
        print("The lab applauds your discovery.")
    else:
        print(f"You, {scientist_name}, dispose of the mixture safely.")
        print("No harm done, but you missed a potential breakthrough.")

# Outcome
print(f"Congratulations, {scientist_name}! You have made significant discoveries in the lab.")
