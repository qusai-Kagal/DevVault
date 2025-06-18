# 📡 Day 26 - NATO Phonetic Alphabet Converter
# Angela Yu's 100 Days of Code - Python Bootcamp
# Advanced Dictionary & List Comprehensions with Real-World Data

# ============================================================================
# 📚 LEARNING OBJECTIVES:
# - Master advanced dictionary comprehensions with pandas DataFrames
# - Understand iterrows() method for efficient row iteration
# - Combine multiple comprehension techniques in real applications
# - Process structured CSV data for practical use cases
# - Handle user input validation and string transformations
# - Build communication tools using NATO standards
# ============================================================================

# 📦 Import required libraries
import pandas  # For CSV data handling and DataFrame operations

# ============================================================================
# 📊 DATA LOADING - NATO Phonetic Alphabet CSV
# ============================================================================

# 📖 Load NATO phonetic alphabet data from CSV file
# CSV structure: letter, code (e.g., A -> Alfa, B -> Bravo)
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# ============================================================================
# 🗂️ TODO 1: DICTIONARY COMPREHENSION - Create Phonetic Dictionary
# ============================================================================

# 📝 Keyword Method with iterrows() - Advanced Dictionary Comprehension
# Syntax: {new_key:new_value for (index, row) in df.iterrows()}

# 🔤 Create a dictionary mapping each letter to its phonetic code word
# iterrows() returns (index, row) tuples for each DataFrame row
# row.letter accesses the 'letter' column, row.code accesses the 'code' column
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# 🧪 Example output: {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', ...}

# ============================================================================
# 💬 TODO 2: MAIN PROGRAM LOOP - Interactive Phonetic Converter
# ============================================================================

# 🔄 Continuous operation until user chooses to exit
while True:
    # 🎤 Get user input and convert to uppercase for consistent matching
    # .upper() ensures all letters match the uppercase keys in our dictionary
    word = input("Enter a word (or 'E' to exit): ").upper()

    # 🚪 EXIT CONDITION - Check if user wants to quit
    if word == 'E':
        print("👋 Goodbye! Thanks for using NATO Phonetic Converter!")
        break  # Exit the program loop

    # 🛡️ INPUT VALIDATION - Handle non-alphabetic characters
    # Filter out spaces, numbers, and special characters for clean processing
    clean_word = ''.join([char for char in word if char.isalpha()])

    # ⚠️ Check if word contains any valid letters
    if not clean_word:
        print("❌ Please enter a valid word with letters!")
        continue  # Skip to next iteration

    # 📻 Create list of phonetic code words using list comprehension
    # For each letter in the input word, look up its phonetic equivalent
    # phonetic_dict[letter] retrieves the NATO code for each letter
    output_list = [phonetic_dict[letter] for letter in clean_word]

    # 📢 Display the phonetic conversion with formatted output
    print(f"📡 Phonetic conversion for '{clean_word}':")
    print(" - ".join(output_list))
    print()  # Add blank line for better readability

# ============================================================================
# 🎯 KEY CONCEPTS DEMONSTRATED:
# - pandas.iterrows() for DataFrame row iteration
# - Dictionary comprehension with DataFrame data
# - List comprehension for data transformation
# - While loops with exit conditions
# - User input validation and error handling
# - String methods (.upper(), .isalpha()) for data consistency
# - CSV data processing with pandas
# - Dictionary lookup operations
# - Interactive program flow control
# ============================================================================

# 💡 REAL-WORLD APPLICATION EXAMPLES:
# Input: "HELP"    → ['Hotel', 'Echo', 'Lima', 'Papa']
# Input: "PYTHON"  → ['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
# Input: "SOS"     → ['Sierra', 'Oscar', 'Sierra']
#
# 🎖️ Military/Aviation Use: Clear radio communication
# 🏢 Business Use: Spelling names/codes over phone calls
# 🚨 Emergency Use: Accurate information transmission

# 🚀 PROGRAM FEATURES:
# ============================================================================

# 🔤 CORE FUNCTIONALITY:
# ✅ Instant letter-to-phonetic conversion
# ✅ Case-insensitive input handling (.upper() normalization)
# ✅ Complete NATO alphabet coverage (A-Z)
# ✅ Real-time processing with list comprehensions

# 🔄 INTERACTIVE FEATURES:
# ✅ Continuous operation with while loop
# ✅ Easy exit with 'E' key press
# ✅ User-friendly prompts and feedback
# ✅ Clean program termination with goodbye message

# 📊 DATA HANDLING:
# ✅ CSV-based phonetic alphabet storage
# ✅ Pandas DataFrame integration for efficient lookups
# ✅ Memory-optimized dictionary creation with iterrows()

# 🛡️ ERROR HANDLING:
# ✅ Input validation for non-alphabetic characters
# ✅ Empty input detection and user guidance
# ✅ Graceful handling of invalid entries
# ✅ Continue loop operation after errors

# 🎯 USER EXPERIENCE:
# ✅ Multiple word conversion capability
# ✅ Clean formatted output with separators
# ✅ Visual feedback with emojis and clear messages
# ✅ Professional communication standard compliance

# 🏆 PYTHON MASTERY ACHIEVED:
# ✅ Advanced dictionary comprehensions with DataFrame integration
# ✅ Efficient list comprehensions for data transformation
# ✅ Professional-grade pandas data processing techniques
# ✅ Clean, maintainable, and Pythonic code architecture
# ✅ Real-world communication tool development

# 📝 CHALLENGE MASTERED: Built a professional NATO phonetic converter using
# cutting-edge comprehensions and enterprise-level pandas operations!