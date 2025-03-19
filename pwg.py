#!/usr/bin/env python3

import argparse
import random
import string
import subprocess
import sys


def generate_strong_password(length: int, special_characters: bool) -> str:
    if length < 8:
        length = 8
        print("It ain't gonna be a strong password with that little symbols")
    else:
        character_base = string.ascii_letters + string.digits if not special_characters \
                    else string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(character_base, k=length))

def copy_to_clipboard(string_to_copy: str) -> None:
    if sys.platform == "win32":
        subprocess.run("clip", input=string_to_copy.strip().encode(), check=True)
    elif sys.platform == "linux":
        subprocess.run("xclip -selection clipboard",
                       input=string_to_copy.strip().encode(),
                       shell=True, check=True)

def pwg():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("-l", "--length", type=int, default=8,
                        help="Length of your password (8 by default)")
    parser.add_argument("-ns", "--no-special", action="store_false",
                        help="Exclude special characters")
    
    args = parser.parse_args()

    password = generate_strong_password(args.length, args.no_special)
    copy_to_clipboard(password)

    print(f"Your password is copied to clipboard")

if __name__ == "__main__":
    pwg()