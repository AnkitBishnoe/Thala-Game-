def convert_to_7(number):
    """
    Convert any number to 7 using only the user's input number with arithmetic operations
    """
    num = abs(int(number))
    
    if num == 7:
        return ["Already 7! 🎉"]
    
    steps = []
    current = num
    
    # Keep summing digits of the user's number until we reach 7
    while current != 7 and len(steps) < 20:
        if current < 10:
            # Single digit: direct addition or subtraction to reach 7
            if current < 7:
                diff = 7 - current
                steps.append(f"{current} + {diff} = 7")
            else:
                diff = current - 7
                steps.append(f"{current} - {diff} = 7")
            current = 7
        else:
            # Multiple digits: sum them together
            digits = [int(d) for d in str(current)]
            digit_sum = sum(digits)
            operation = " + ".join(str(d) for d in digits)
            steps.append(f"{current} → {operation} = {digit_sum}")
            current = digit_sum
    
    return steps


def display_game():
    """Main game loop"""
    print("=" * 60)
    print("🎮 WELCOME TO THE 'CONVERT TO 7' GAME! 🎮")
    print("=" * 60)
    print("\nRules: Enter any number, and I'll convert it to 7")
    print("using simple arithmetic operations!")
    print("\n" + "=" * 60)
    
    while True:
        print("\n")
        user_input = input("🔢 Enter a number (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            print("\n🎉 Thanks for playing! Goodbye! 👋")
            break
        
        try:
            number = int(user_input)
            print(f"\n✨ Converting {number} to 7... ✨\n")
            
            steps = convert_to_7(number)
            
            # Display the conversion process
            for i, operation in enumerate(steps, 1):
                print(f"Step {i}: {operation}")
            
            print(f"\n🎯 SUCCESS! We reached 7! 🎯\n")
            print("─" * 60)
            
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    display_game()
