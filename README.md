
# Caesar's Cipher
This is a Python project that implements a menu for encoding and decoding text using the Caesar cipher.

## Overview
The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each character in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You need to have Python installed on your machine. You can check if you have Python installed, and the version of it, by running the following command in your terminal:

```
python --version
```

### Installing
Clone the repository to your local machine:

```
git clone git@github.com:shukla-0007/Caesars-Cipher.git
```

### Running the Project
1. **Navigate to the project directory:**
   ```
   cd Caesars_Cipher
   ```
2. **Run the Python script:**
   ```
   python main.py
   ```
   This will start the Caesar cipher encoding/decoding menu.

### Notes
- Ensure you have Python installed on your system. Most systems come with Python pre-installed, but you can download it from [python.org](https://www.python.org/) if needed.
- Make sure the `main.py` file is in the same directory as the rest of your project files.

### Example Use Cases
- **Encode a message:** Select option 1 and enter your text and shift key.
- **Decode a message:** Select option 2 and enter your encoded text and shift key.

### Contributing
Contributions are welcome! Feel free to submit pull requests or open issues if you encounter any bugs or have suggestions for improvements.

## Features
- **Menu-driven interface:** Easy to use with options for encoding, decoding, and exiting.
- **Caesar Cipher implementation:** Supports both uppercase and lowercase letters, preserving case during encoding and decoding.
- **Non-alphabetical characters:** Leaves non-alphabetical characters unchanged.

## Known Issues
- Currently does not handle non-English alphabets.

## Future Development
- Support for other encryption techniques.
- Handling of non-English alphabets.
- Input validation for non-alphabetical characters.
