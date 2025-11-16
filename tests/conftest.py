import sys
from pathlib import Path
import importlib.util

project_root = Path(__file__).parent.parent
src_path = project_root / "src" / "utils" / "utils.py"

spec = importlib.util.spec_from_file_location("utils.utils", src_path)
utils_module = importlib.util.module_from_spec(spec)
sys.modules["utils.utils"] = utils_module
spec.loader.exec_module(utils_module)

