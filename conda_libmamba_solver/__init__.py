"""
We offer two implementations:

- LibMambaSolverDraft was the first one, and it depends on the full mamba distribution. It's only kept
  around for debugging purposes and will be eventually deprecated and removed.
- LibMambaSolver is a refactor of the latter, and only depends on libmambapy (the wrapped C++ library).
  This is the one we will eventually ship as final.
"""

__version__ = "22.3.1"

from ._libmamba import LibMambaSolverDraft
from .solver import LibMambaSolver


def get_solver_class(key=None):
    return {
        "libmamba-draft": LibMambaSolverDraft,
        "libmamba": LibMambaSolver,
    }[key]
