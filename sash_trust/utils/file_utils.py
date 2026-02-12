from pathlib import Path


def safe_read_text(path: Path) -> str:
    """
    Safe file reader.
    Prevents crash on binary files.
    """
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
