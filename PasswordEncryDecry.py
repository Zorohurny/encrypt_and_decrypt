import time
import os
import sys

# Banner to show after loading animation
BANNER = '''
████████████████████████████████████████████████
█░░░░░░░░░░░░░░██████████████████████░░░░░░░░███
█░░▄▀▄▀▄▀▄▀▄▀░░██████████████████████░░▄▀▄▀░░███
█░░░░░░░░░░▄▀░░████████░░░░░░████████░░░░▄▀░░███
█████████░░▄▀░░████████░░▄▀░░██████████░░▄▀░░███
█░░░░░░░░░░▄▀░░████░░░░░░▄▀░░░░░░██████░░▄▀░░███
█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀░░███
█░░░░░░░░░░▄▀░░████░░░░░░▄▀░░░░░░██████░░▄▀░░███
█████████░░▄▀░░████████░░▄▀░░██████████░░▄▀░░███
█░░░░░░░░░░▄▀░░████████░░░░░░████████░░░░▄▀░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░██████████████████████░░▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░██████████████████████░░░░░░░░░░█
████████████████████████████████████████████████

Note: Password must be at least 8 characters
'''

# Menu options
OPTIONS = '''
1. Encryption 
2. Decryption
3. Exit
:- '''


def encrypt_password():
    """Encrypt the input password with a simple obfuscation logic."""
    password = input("Enter Password :- ")
    if len(password) < 8:
        print("❌ Password must be at least 8 characters.\n")
        return

    encrypted = f"{password[3]}{password[-3:]}{password[4:-3]}{password[:3]}"
    print("\n🔐 Encrypted Password:", encrypted, "\n")


def decrypt_password():
    """Decrypt the previously encrypted password."""
    encrypted = input("Enter Password :- ")
    if len(encrypted) < 8:
        print("❌ Invalid input.\n")
        return

    first_3 = encrypted[1:4]
    fourth = encrypted[0]
    middle = encrypted[4:-3]
    last_3 = encrypted[-3:]

    original = f"{last_3}{fourth}{middle}{first_3}"
    print("\n🔓 Decrypted Password:", original, "\n")


def loading_animation(duration=2, interval=0.1):
    """Display a loading animation for a given duration."""
    start_time = time.time()
    animation = [
        "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]",
        "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
        "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]",
        "[■■■■■■■■■■]"
    ]

    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        progress = min(1.0, elapsed / duration)
        symbol = animation[int(progress * len(animation)) % len(animation)]
        sys.stdout.write(f"\rLoading: {symbol} {progress:.1%}")
        sys.stdout.flush()
        time.sleep(interval)

    os.system("cls" if os.name == "nt" else "clear")
    print(BANNER)


# --- Main Program ---
if __name__ == "__main__":
    loading_animation()

    while True:
        choice = input(OPTIONS).strip()
        if choice == "1":
            encrypt_password()
        elif choice == "2":
            decrypt_password()
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Please select a valid option (1/2/3).\n")
