"""A small command-line greeting application."""

import argparse


def greet(name: str, *, shout: bool = False) -> str:
    """Return a friendly greeting for *name*.

    Set ``shout`` to make the message uppercase.
    """
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Name cannot be empty.")
    message = f"Hello, {clean_name}!"
    return message.upper() if shout else message


def parse_args() -> argparse.Namespace:
    """Read optional command-line arguments."""
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("name", nargs="?", help="The person to greet")
    parser.add_argument(
        "--shout",
        action="store_true",
        help="Print the greeting in uppercase",
    )
    return parser.parse_args()


def main() -> None:
    """Run the application."""
    args = parse_args()
    name = args.name or input("What is your name? ").strip()

    try:
        print(greet(name, shout=args.shout))
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
