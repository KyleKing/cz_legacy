"""Check that all imports work as expected.

Primarily checking that:

1. No optional dependencies are required

FIXME: Replace with programmatic imports? Maybe explicit imports to check backward compatibility of public API?
    https://stackoverflow.com/questions/34855071/importing-all-functions-from-a-package-from-import

"""

# FYI: Cannot import _LegacyCz or discover_this because would cause a circular import
