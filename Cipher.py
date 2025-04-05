class Cipher:
    def encode(str, shift):
        encoded = ""
        for ch in str:
            if ch.isalpha():
                base = 'A' if ch.isupper() else 'a'
                encoded += chr((ord(ch) - ord(base) + shift) % 26 + ord(base))
            else:
                encoded += ch
        return encoded

    def decode(str, shift):
        return Cipher.encode(str, 26 - (shift % 26))


def main():
    while True:
        print("Caesar Cipher Menu:")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            encode_str = input("Enter the string to encode: ")
            while True:
                try:
                    encode_key = int(input("Enter the shift key: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            encoded = Cipher.encode(encode_str, encode_key)
            print("Encoded string:", encoded)

        elif choice == "2":
            decode_str = input("Enter the string to decode: ")
            while True:
                try:
                    decode_key = int(input("Enter the shift key: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            decoded = Cipher.decode(decode_str, decode_key)
            print("Decoded string:", decoded)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
