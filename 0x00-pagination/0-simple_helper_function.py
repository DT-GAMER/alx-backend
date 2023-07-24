#!/usr/bin/env python3
"""
contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    calculate the start and the end index for pagination.

    Args:
        page (int): The 1-indexed page number.
        page_size (int): The size of each page.

    Returns:
        tuple: A tuple containing the start index (inclusive) and the end index (exclusive).
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page size must be positive integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
