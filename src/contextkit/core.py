"""Context composition helpers."""


def trim(text: str, max_chars: int) -> str:
    """Keep the first max_chars characters."""
    if max_chars < 0:
        raise ValueError("max_chars must be non-negative")
    return text[:max_chars]


def merge(parts: list[str], separator: str = "\n\n") -> str:
    """Join non-empty context parts."""
    return separator.join(part.strip() for part in parts if part.strip())
