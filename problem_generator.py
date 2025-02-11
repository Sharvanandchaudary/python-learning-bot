import random

def generate_problem():
    problems = [
        # Array
        {"question": "Find the maximum product of two integers in an array", "difficulty": "Medium", "link": "https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/"},
        {"question": "Move zeroes to the end of the array", "difficulty": "Easy", "link": "https://leetcode.com/problems/move-zeroes/"},
        {"question": "Rotate an array", "difficulty": "Medium", "link": "https://leetcode.com/problems/rotate-array/"},
        {"question": "Find the intersection of two arrays", "difficulty": "Easy", "link": "https://leetcode.com/problems/intersection-of-two-arrays/"},
        {"question": "Set matrix zeroes", "difficulty": "Medium", "link": "https://leetcode.com/problems/set-matrix-zeroes/"},
        {"question": "Merge intervals", "difficulty": "Hard", "link": "https://leetcode.com/problems/merge-intervals/"},
        {"question": "Find the kth largest element in an array", "difficulty": "Medium", "link": "https://leetcode.com/problems/kth-largest-element-in-an-array/"},
        {"question": "Spiral matrix", "difficulty": "Medium", "link": "https://leetcode.com/problems/spiral-matrix/"},
        {"question": "3Sum", "difficulty": "Medium", "link": "https://leetcode.com/problems/3sum/"},
        {"question": "Container with most water", "difficulty": "Hard", "link": "https://leetcode.com/problems/container-with-most-water/"},
        {"question": "Subarray sum equals K", "difficulty": "Medium", "link": "https://leetcode.com/problems/subarray-sum-equals-k/"},
        
        # String
        {"question": "Reverse a string", "difficulty": "Easy", "link": "https://leetcode.com/problems/reverse-string/"},
        {"question": "Check if a string is a palindrome", "difficulty": "Easy", "link": "https://leetcode.com/problems/valid-palindrome/"},
        {"question": "Implement strStr()", "difficulty": "Easy", "link": "https://leetcode.com/problems/implement-strstr/"},
        {"question": "Longest palindromic substring", "difficulty": "Medium", "link": "https://leetcode.com/problems/longest-palindromic-substring/"},
        {"question": "Valid Anagram", "difficulty": "Easy", "link": "https://leetcode.com/problems/valid-anagram/"},
        {"question": "Group anagrams", "difficulty": "Medium", "link": "https://leetcode.com/problems/group-anagrams/"},
        {"question": "Longest common prefix", "difficulty": "Easy", "link": "https://leetcode.com/problems/longest-common-prefix/"},
        {"question": "Decode Ways", "difficulty": "Medium", "link": "https://leetcode.com/problems/decode-ways/"},
        {"question": "String to Integer (atoi)", "difficulty": "Medium", "link": "https://leetcode.com/problems/string-to-integer-atoi/"},
        {"question": "Find the first non-repeating character in a string", "difficulty": "Medium", "link": "https://leetcode.com/problems/first-unique-character-in-a-string/"},
        
        # Math
        {"question": "Add two numbers represented by linked lists", "difficulty": "Medium", "link": "https://leetcode.com/problems/add-two-numbers/"},
        {"question": "Palindrome number", "difficulty": "Easy", "link": "https://leetcode.com/problems/palindrome-number/"},
        {"question": "Sqrt(x)", "difficulty": "Easy", "link": "https://leetcode.com/problems/sqrtx/"},
        {"question": "Roman to Integer", "difficulty": "Easy", "link": "https://leetcode.com/problems/roman-to-integer/"},
        {"question": "Integer to Roman", "difficulty": "Medium", "link": "https://leetcode.com/problems/integer-to-roman/"},
        {"question": "Climbing stairs", "difficulty": "Medium", "link": "https://leetcode.com/problems/climbing-stairs/"},
        {"question": "Fibonacci number", "difficulty": "Easy", "link": "https://leetcode.com/problems/fibonacci-number/"},
        {"question": "Count and Say", "difficulty": "Medium", "link": "https://leetcode.com/problems/count-and-say/"},
        {"question": "Factorial Trailing Zeroes", "difficulty": "Medium", "link": "https://leetcode.com/problems/factorial-trailing-zeroes/"},
        {"question": "Excel Sheet Column Number", "difficulty": "Easy", "link": "https://leetcode.com/problems/excel-sheet-column-number/"},
        
        # Dynamic Programming
        {"question": "Coin Change", "difficulty": "Medium", "link": "https://leetcode.com/problems/coin-change/"},
        {"question": "House Robber", "difficulty": "Medium", "link": "https://leetcode.com/problems/house-robber/"},
        {"question": "Longest Increasing Subsequence", "difficulty": "Medium", "link": "https://leetcode.com/problems/longest-increasing-subsequence/"},
        {"question": "Word Break", "difficulty": "Medium", "link": "https://leetcode.com/problems/word-break/"},
        {"question": "Combination Sum IV", "difficulty": "Medium", "link": "https://leetcode.com/problems/combination-sum-iv/"},
        {"question": "Maximum Subarray", "difficulty": "Medium", "link": "https://leetcode.com/problems/maximum-subarray/"},
        {"question": "Decode Ways II", "difficulty": "Hard", "link": "https://leetcode.com/problems/decode-ways-ii/"},
        {"question": "Burst Balloons", "difficulty": "Hard", "link": "https://leetcode.com/problems/burst-balloons/"},
        {"question": "Palindrome Partitioning II", "difficulty": "Hard", "link": "https://leetcode.com/problems/palindrome-partitioning-ii/"},
        {"question": "Scramble String", "difficulty": "Hard", "link": "https://leetcode.com/problems/scramble-string/"},
        
        # Miscellaneous
        {"question": "N-Queens", "difficulty": "Hard", "link": "https://leetcode.com/problems/n-queens/"},
        {"question": "Sudoku Solver", "difficulty": "Hard", "link": "https://leetcode.com/problems/sudoku-solver/"},
        {"question": "Clone Graph", "difficulty": "Medium", "link": "https://leetcode.com/problems/clone-graph/"},
        {"question": "Graph Valid Tree", "difficulty": "Medium", "link": "https://leetcode.com/problems/graph-valid-tree/"},
        {"question": "Find the Celebrity", "difficulty": "Hard", "link": "https://leetcode.com/problems/find-the-celebrity/"},
        {"question": "Alien Dictionary", "difficulty": "Hard", "link": "https://leetcode.com/problems/alien-dictionary/"},
        {"question": "Minimum Window Substring", "difficulty": "Hard", "link": "https://leetcode.com/problems/minimum-window-substring/"},
        {"question": "Largest Rectangle in Histogram", "difficulty": "Hard", "link": "https://leetcode.com/problems/largest-rectangle-in-histogram/"},
        {"question": "Merge k Sorted Lists", "difficulty": "Hard", "link": "https://leetcode.com/problems/merge-k-sorted-lists/"},
        {"question": "Word Search II", "difficulty": "Hard", "link": "https://leetcode.com/problems/word-search-ii/"},
    ]
    
    # Randomly select a problem
    problem = random.choice(problems)
    return problem
