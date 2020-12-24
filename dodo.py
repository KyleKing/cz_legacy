"""doit Script."""

from pathlib import Path

from calcipy.doit_tasks import *  # noqa: F401,F403,H303 (Run 'doit list' to see tasks). skipcq: PYL-W0614
from calcipy.doit_tasks.doit_globals import DIG

# Configure source code root path
path_parent = Path(__file__).resolve().parent
DIG.set_paths(path_project=path_parent)

# Create list of all tasks run with `poetry run doit`
DOIT_CONFIG = {
    'action_string_formatting': 'old',
    'default_tasks': [
        'cl_write',
        'create_tag_file',
        'coverage',
        'auto_format',
        'pre_commit_hooks',
        'lint_critical_only',
    ],
}
