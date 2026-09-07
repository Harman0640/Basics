"""Application entry point."""


def greet(name: str) -> str:
    """Return a friendly greeting for *name*."""
    return f"Hello, {name}!"


def main() -> None:
    """Run the application."""
    print(greet("World"))


if __name__ == "__main__":
    main()
