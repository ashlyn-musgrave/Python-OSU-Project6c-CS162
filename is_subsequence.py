# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/26/2023
# Description: This program takes two string parameters and returns True if the first
# string is a subsequence of the second string, but returns False otherwise.
def is_subsequence(A,B):
    """This function returns True if the first string is a subsequence of the second string, but returns
    False otherwise
  """
    # We know that if the length of A is 0, meaning it's nothing, then it exists in B and is therefore True
    if len(A)==0:
        return True
    # We know that if the length of B is zero, then there's no way A can be found in B and is therefore False
    if len(B)==0:
        return False

    if A[-1]==B[-1]:

        return is_subsequence(A[:-1],B[:-1])

    return is_subsequence(A,B[:-1])

