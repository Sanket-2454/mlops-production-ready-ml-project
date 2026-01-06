import logging
import os  



from pathlib import Path

def from_root(*paths):
    """Return project root path or a sub-path inside it.

    Searches upward for common project markers (`pyproject.toml`, `setup.py`, `.git`) and
    falls back to the filesystem root if none are found.
    """
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / 'pyproject.toml').exists() or (parent / 'setup.py').exists() or (parent / '.git').exists():
            root = parent
            break
    else:
        root = p.parents[-1]
    return str(root.joinpath(*paths)) if paths else str(root)
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(os.path.join(from_root(), log_dir), exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)