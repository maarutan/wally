import sys, os
from pathlib import Path
from shutil import which

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.dependencies import check_your_session_type

if __name__ == "__main__":
    check_your_session_type()
