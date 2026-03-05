from datetime import datetime


def main() -> None:
    print(f"Hello from project inside .venv at {datetime.now().isoformat(timespec='seconds')}")


if __name__ == "__main__":
    main()
