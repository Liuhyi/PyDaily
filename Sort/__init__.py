from .base import Sorter
from .hoare_quicksort import HoareSorter
from .lomuto_quicksort import LomutoSorter
from .threeway_quicksort import ThreeWaySorter
from .merge_sort import MergeSorter
sorters = [
    Sorter,
    HoareSorter,
    LomutoSorter,
    ThreeWaySorter,
    MergeSorter
]

