# Import the art module to display ASCII art logo
import art

# Display the logo at the start of the program
print(art.logo)

# Define the alphabet list for character mapping
# This contains all lowercase letters from 'a' to 'z'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    """
    Caesar cipher function that can both encode and decode text.
    
    Parameters:
    original_text (str): The text to be encoded or decoded
    shift_amount (int): The number of positions to shift each letter
    encode_or_decode (str): Either "encode" or "decode" to specify operation
    """
    # Initialize empty string to store the result
    output_text = ""
    
    # If decoding, make the shift negative to reverse the encoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Process each character in the input text
    for letter in original_text:
        
        # If the character is not in the alphabet (spaces, punctuation, numbers)
        # keep it unchanged
        if letter not in alphabet:
            output_text += letter
        else:
            # Find the current position of the letter in the alphabet
            shifted_position = alphabet.index(letter) + shift_amount
            
            # Use modulo to wrap around the alphabet (z + 1 = a)
            # This ensures we stay within the bounds of the alphabet
            shifted_position %= len(alphabet)
            
            # Add the shifted letter to the output
            output_text += alphabet[shifted_position]
    
    # Display the result to the user
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Main program loop - allows multiple operations without restarting
should_continue = True

while should_continue:
    
    # Get user input for operation type (encode or decode)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    # Get the message to be processed
    text = input("Type your message:\n").lower()
    
    # Get the shift amount (how many positions to move each letter)
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function with user inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if the user wants to perform another operation
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    
    # Exit the loop if user doesn't want to continue
    if restart == "no":
        should_continue = False
        print("Goodbye")