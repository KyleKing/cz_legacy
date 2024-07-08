"""cz_legacy."""

from contextlib import suppress

with suppress(ImportError):
    # Make the beartype dependency optional
    from ._runtime_type_check_setup import configure_runtime_type_checking_mode

    configure_runtime_type_checking_mode()

__version__ = '2.0.2'
__pkg_name__ = 'cz_legacy'


# == Above code must always be first ==
