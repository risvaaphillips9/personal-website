"""
Pytest stability for CI environments.

Some GitHub-hosted runners preload third-party pytest plugins that can cause
unexpected collection or usage errors. Disable auto-loading of external plugins
so our tests only run with pytest's built-ins unless explicitly enabled.
"""

import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

