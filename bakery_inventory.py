
def load_inventory():
    return {}


def parse_kv(input_text):
        key, value = input_text.split(" ", 1)
        return key.strip(), value.strip()
    parts = input_text.strip().split(maxsplit=1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    raise ValueError("Enter as 'item amount'")


def cmd_add(inventory, args):
    try:
        key, value = parse_kv(" ".join(args) if args else input("Enter item and amount (e.g., 'flour 10kg'): "))
    except ValueError as e:
        print(e)
        return
    inventory[key] = value
    print(f"Saved: {key} -> {value}")


def cmd_view(inventory, _args):
    if not inventory:
        print("Inventory is empty.")
        return
    width = max(len(k) for k in inventory.keys())
    for key in sorted(inventory.keys()):
        print(f"{key.ljust(width)} : {inventory[key]}")


def cmd_search(inventory, args):
    if not args:
        query = input("Search term: ").strip()
    else:
        query = " ".join(args).strip()
    matches = {k: v for k, v in inventory.items() if query in k}
    if not matches:
        print("No matches.")
        return
    width = max(len(k) for k in matches.keys())
    for key in sorted(matches.keys()):
        print(f"{key.ljust(width)} : {matches[key]}")


def cmd_delete(inventory, args):
    key = " ".join(args) if args else input("Item to delete: ").strip()
    if key in inventory:
        removed = inventory.pop(key)
        print(f"Deleted: {key} (was {removed})")
    else:
        print("Item not found.")


def cmd_help(_inventory, _args):
    print(
        "Commands:\n"
        "  add [item amount]  - Add or update an item (e.g., 'add flour 10kg')\n"
        "  view                - Show all inventory\n"
        "  search something       - Search items\n"
        "  exit       - exit\n"
    )


def repl():
    inventory = load_inventory()
    print("Bakery Inventory. Type 'help' for commands.")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not raw:
            continue

        parts = raw.split()
        command, args = parts[0].lower(), parts[1:]

        if command in {"exit"}:
            break
        elif command == "add":
            cmd_add(inventory, args)
        elif command == "view":
            cmd_view(inventory, args)
        elif command == "search":
        else:
            print("Error")


if __name__ == "__main__":
    repl()


