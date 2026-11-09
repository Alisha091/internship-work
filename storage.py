"""JSON file storage for expenses. No input() or print() here."""

import json


def load_expenses(path):
    """Read expenses from a JSON file.

    Returns (expenses, error_message). A missing file is not an error:
    it returns an empty list and None.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return [], None
    except PermissionError:
        return [], f"Permission denied: cannot read '{path}'."
    except json.JSONDecodeError:
        return [], f"'{path}' contains malformed JSON. Starting with an empty list."

    if not isinstance(data, list):
        return [], f"'{path}' must contain a list of expenses. Starting with an empty list."
    for record in data:
        if not isinstance(record, dict) or not {"description", "amount", "category"} <= record.keys():
            return [], f"'{path}' has an invalid expense record. Starting with an empty list."
    return data, None


def save_expenses(path, expenses):
    """Write expenses to a JSON file. Return an error message, or None if saved."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=2)
    except PermissionError:
        return f"Permission denied: cannot write '{path}'."
    except OSError as error:
        return f"Could not save '{path}': {error}"
    return None