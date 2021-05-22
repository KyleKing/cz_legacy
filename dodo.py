"""doit Script.

```sh
# Ensure that packages are installed
poetry install
# List Tasks
poetry run doit list
# (Or use a poetry shell)
# > poetry shell
# > doit list

# Run tasks individually (examples below)
poetry doit run coverage open_test_docs
poetry doit run set_lint_config create_tag_file document
# Or all of the tasks in DOIT_CONFIG
poetry run doit
```

"""

from pathlib import Path

from calcipy.doit_tasks import *  # noqa: F401,F403,H303 (Run 'doit list' to see tasks). skipcq: PYL-W0614
from calcipy.doit_tasks import DOIT_CONFIG_RECOMMENDED
from calcipy.doit_tasks.doit_globals import DIG

# Configure source code root path
path_parent = Path(__file__).resolve().parent
DIG.set_paths(path_project=path_parent)

# Create list of all tasks run with `poetry run doit`
DOIT_CONFIG = DOIT_CONFIG_RECOMMENDED
