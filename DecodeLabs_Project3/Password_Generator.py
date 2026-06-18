import secrets
import string
print("          +----------------------+")
print("          | PASSWORD GENERATOR   |")
print("          +----------------------+")
def generate_password(length: int, include_special: bool = True) -> str:
    # Validate input
    if not isinstance(length, int) or length < 1:
        raise ValueError("Password length must be a positive integer.")
    
  
    char_pool = string.ascii_letters + string.digits
    if include_special:
        char_pool += string.punctuation

    # Generate password
    password_chars = [secrets.choice(char_pool) for _ in range(length)]

    # Ensure at least one digit
    if not any(ch.isdigit() for ch in password_chars):
        password_chars[0] = secrets.choice(string.digits)

    # Efficient join pattern
    password = ''.join(password_chars)
    return password


if __name__ == "__main__":
    try:
        user_length = int(input("Enter desired password length: "))
        choice = input("Include special characters? (y/n): ").strip().lower()
        include_special = choice == 'y'
        secure_password = generate_password(user_length, include_special)
        print(f"Generated Password: {secure_password}")
    except ValueError as e:
        print(f"Error: {e}")

