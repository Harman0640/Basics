"""A small command-line greeting application."""

import argparse


def greet(name: str) -> str:
    """Return a friendly greeting for *name*."""
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Name cannot be empty.")
    return f"Hello, {clean_name}!"


def parse_args() -> argparse.Namespace:
    """Read optional command-line arguments."""
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("name", nargs="?", help="The person to greet")
    return parser.parse_args()


def main() -> None:
    """Run the application."""
    args = parse_args()
    name = args.name or input("What is your name? ").strip()

    try:
        print(greet(name))
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
