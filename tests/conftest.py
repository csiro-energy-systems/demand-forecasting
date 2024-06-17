import sys
from pathlib import Path

# Add the root directory to sys.path to make the src module importable
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
