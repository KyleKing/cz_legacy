"""cz_legacy."""

from importlib.metadata import EntryPoint

__version__ = '0.1.7'
__pkg_name__ = 'cz_legacy'

EntryPoint(name='cz_legacy', value='cz_legacy.cz_legacy:_LegacyCz', group='commitizen.plugin')
"""Make the _LegacyCz class discoverable by commitizen."""
