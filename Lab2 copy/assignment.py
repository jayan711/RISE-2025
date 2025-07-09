## assignment.py
"""Lab July 2 — core functions to implement.

Edit *only* the bodies that contain `raise NotImplementedError()`.
Do **not** rename functions: the autograder expects these names.
"""

from __future__ import annotations
from typing import Iterable, Dict, List
import math


def _validate_numeric(nums: Iterable[float]) -> List[float]:
    """Return a concrete list after validating elements are numeric."""
    nums = list(nums)
    if not nums:
        raise ValueError("Input sequence is empty.")
    for x in nums:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Non‑numeric element detected: {x!r}")
    return nums


def mean_loop(nums: Iterable[float]) -> float:
    """Compute arithmetic mean using an explicit *for* loop.

    Args:
        nums: Sequence of int/float values.
    Returns:
        The mean of the inputs.
    """
    #Validate the List 
    nums = _validate_numeric(nums)

    #For loop to find sum
    summ = 0
    for num in nums:
        summ += num
    
    #Return mean
    return summ / len(nums)


def median_loop(nums: Iterable[float]) -> float:
    """Return the median value without using `statistics` or `numpy`."""
    
    #Validate the List
    nums = _validate_numeric(nums)

    #Sort the List
    nums = sorted(nums)

    #Find the Middle Index (integer)
    center = len(nums) // 2

    #Check if list is an even list 
    if (len(nums) % 2 == 0):
        #If it is, add two middle numbers and divide by 2 (take the average)
        return (nums[center] + nums[center - 1]) / 2
    
    #Else it is an odd list
    else:
        return nums[center]

def summary_stats(nums: Iterable[float]) -> Dict[str, float]:
    """Return mean, median, min, and max as a dictionary."""
    
    #Validate the List
    nums = _validate_numeric(nums)

    #Sort the List
    nums = sorted(nums)

    #Initialize a dicitonary and add mean, median, min, and max (using the functions)
    summary = {"mean" : mean_loop(nums), "median" : median_loop(nums), "min" : nums[0], "max" : nums[len(nums) - 1]}
    return summary

def quantile(nums: Iterable[float], q: float) -> float:
    """Compute the *q*‑quantile (0 ≤ q ≤ 1) via linear interpolation."""
    
    #Validate the List
    nums = _validate_numeric(nums)
    
    #Sort the List
    nums = sorted(nums)
    
    #Calculate the index (of the list) using the given quantile
    quan = (len(nums) - 1) * q

    #Lower Index
    x1 = int(quan)

    #Upper Index 
    x2 = math.ceil(quan)

    #Corresponding values
    y1 = nums[x1]
    y2 = nums[x2]

    #If the calculated index is an integer, return the value corresponding to the index
    if (x1 == x2):
        return y1
    #Else, use linear interpolation to calculate the value
    else:
        return y1 + ((quan - x1) * (y2 - y1)) / (x2 - x1)



