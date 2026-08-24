from app.database import SessionLocal
from app.models import Problem


problems = [
    {
        "title": "Two Sum",
        "description": "Given an array of integers and a target value, return the indices of two numbers whose sum equals the target.",
        "difficulty": "Easy",
        "input_format": "The first line contains n and target. The second line contains n integers.",
        "output_format": "Print the two indices of the elements whose sum equals the target.",
        "constraints": "2 <= n <= 10^4; -10^9 <= nums[i] <= 10^9.",
        "sample_input": "4 9\n2 7 11 15",
        "sample_output": "0 1"
    },

    {
        "title": "Maximum Subarray",
        "description": "Given an integer array, find the contiguous subarray with the largest possible sum.",
        "difficulty": "Medium",
        "input_format": "The first line contains n. The second line contains n integers.",
        "output_format": "Print the maximum possible subarray sum.",
        "constraints": "1 <= n <= 10^5; -10^4 <= nums[i] <= 10^4.",
        "sample_input": "9\n-2 1 -3 4 -1 2 1 -5 4",
        "sample_output": "6"
    },

    {
        "title": "Palindrome Number",
        "description": "Determine whether a given integer reads the same forward and backward.",
        "difficulty": "Easy",
        "input_format": "A single integer x.",
        "output_format": "Print YES if x is a palindrome, otherwise print NO.",
        "constraints": "-2^31 <= x <= 2^31 - 1.",
        "sample_input": "121",
        "sample_output": "YES"
    },

    {
        "title": "House Robber",
        "description": "Given the amount of money in each house, determine the maximum amount that can be robbed without robbing two adjacent houses.",
        "difficulty": "Medium",
        "input_format": "The first line contains n. The second line contains n integers.",
        "output_format": "Print the maximum amount that can be robbed.",
        "constraints": "1 <= n <= 10^5; 0 <= nums[i] <= 10^4.",
        "sample_input": "5\n2 7 9 3 1",
        "sample_output": "12"
    },

    {
        "title": "Valid Parentheses",
        "description": "Given a string containing parentheses, brackets and braces, determine whether the brackets are correctly matched and nested.",
        "difficulty": "Easy",
        "input_format": "A single string containing characters (, ), {, }, [ and ].",
        "output_format": "Print YES if the brackets are valid, otherwise print NO.",
        "constraints": "1 <= length of string <= 10^4.",
        "sample_input": "({[]})",
        "sample_output": "YES"
    },

    {
        "title": "Best Time to Buy and Sell Stock",
        "description": "Given daily stock prices, find the maximum profit obtainable by buying once and selling once later.",
        "difficulty": "Easy",
        "input_format": "The first line contains n. The second line contains n stock prices.",
        "output_format": "Print the maximum possible profit.",
        "constraints": "1 <= n <= 10^5; 0 <= prices[i] <= 10^4.",
        "sample_input": "5\n7 1 5 3 6",
        "sample_output": "5"
    },

    {
        "title": "Number of Islands",
        "description": "Given a grid containing land represented by 1 and water represented by 0, count the number of connected islands.",
        "difficulty": "Medium",
        "input_format": "The first line contains rows and columns. The following lines contain the binary grid.",
        "output_format": "Print the number of islands.",
        "constraints": "1 <= rows, columns <= 300.",
        "sample_input": "4 5\n11000\n11000\n00100\n00011",
        "sample_output": "3"
    },

    {
        "title": "Binary Search",
        "description": "Given a sorted array and a target value, find the index of the target using binary search.",
        "difficulty": "Easy",
        "input_format": "The first line contains n and target. The second line contains n sorted integers.",
        "output_format": "Print the index of target, or -1 if it does not exist.",
        "constraints": "1 <= n <= 10^5.",
        "sample_input": "6 9\n1 3 5 7 9 11",
        "sample_output": "4"
    },

    {
        "title": "Longest Substring Without Repeating Characters",
        "description": "Given a string, find the length of the longest substring that contains no repeated characters.",
        "difficulty": "Medium",
        "input_format": "A single string s.",
        "output_format": "Print the length of the longest substring without repeating characters.",
        "constraints": "0 <= length of s <= 10^5.",
        "sample_input": "abcabcbb",
        "sample_output": "3"
    },

    {
        "title": "Move Zeroes",
        "description": "Move all zeroes in an array to the end while maintaining the relative order of non-zero elements.",
        "difficulty": "Easy",
        "input_format": "The first line contains n. The second line contains n integers.",
        "output_format": "Print the modified array.",
        "constraints": "1 <= n <= 10^5.",
        "sample_input": "5\n0 1 0 3 12",
        "sample_output": "1 3 12 0 0"
    },

    {
        "title": "Reverse Integer",
        "description": "Given a signed 32-bit integer, return its digits reversed. Return 0 if the reversed value overflows the 32-bit integer range.",
        "difficulty": "Easy",
        "input_format": "A single integer x.",
        "output_format": "Print the reversed integer, or 0 if it overflows.",
        "constraints": "-2^31 <= x <= 2^31 - 1.",
        "sample_input": "123",
        "sample_output": "321"
    },

    {
        "title": "Container With Most Water",
        "description": "Given an array of heights, find two lines that together with the x-axis form a container holding the maximum amount of water.",
        "difficulty": "Medium",
        "input_format": "The first line contains n. The second line contains n non-negative integers representing heights.",
        "output_format": "Print the maximum amount of water the container can hold.",
        "constraints": "2 <= n <= 10^5; 0 <= height[i] <= 10^4.",
        "sample_input": "9\n1 8 6 2 5 4 8 3 7",
        "sample_output": "49"
    },

    {
        "title": "Valid Anagram",
        "description": "Determine whether two strings are anagrams of each other.",
        "difficulty": "Easy",
        "input_format": "Two lowercase strings.",
        "output_format": "Print YES if they are anagrams, otherwise print NO.",
        "constraints": "1 <= length <= 10^5.",
        "sample_input": "listen\nsilent",
        "sample_output": "YES"
    },

    {
        "title": "Merge Sorted Array",
        "description": "Given two sorted arrays, merge them into one sorted array.",
        "difficulty": "Medium",
        "input_format": "The first line contains n and m. The second and third lines contain the two sorted arrays.",
        "output_format": "Print the merged sorted array.",
        "constraints": "0 <= n,m <= 10^5.",
        "sample_input": "3 3\n1 2 4\n1 3 5",
        "sample_output": "1 1 2 3 4 5"
    },

    {
        "title": "Climbing Stairs",
        "description": "You are climbing a staircase with n steps. You can climb either one or two steps at a time. Find the number of distinct ways to reach the top.",
        "difficulty": "Easy",
        "input_format": "A single integer n.",
        "output_format": "Print the number of distinct ways.",
        "constraints": "1 <= n <= 45.",
        "sample_input": "5",
        "sample_output": "8"
    },

    {
        "title": "Reverse Linked List",
        "description": "Given a singly linked list, reverse the list and print the resulting sequence.",
        "difficulty": "Medium",
        "input_format": "The first line contains n. The second line contains n node values.",
        "output_format": "Print the values of the reversed linked list.",
        "constraints": "1 <= n <= 10^5.",
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "5 4 3 2 1"
    },

    {
        "title": "First Unique Character",
        "description": "Find the index of the first character that appears exactly once in a string.",
        "difficulty": "Easy",
        "input_format": "A single lowercase string.",
        "output_format": "Print the index of the first unique character, or -1 if none exists.",
        "constraints": "1 <= length <= 10^5.",
        "sample_input": "leetcode",
        "sample_output": "0"
    },

    {
        "title": "Linked List Cycle",
        "description": "Determine whether a linked list contains a cycle.",
        "difficulty": "Medium",
        "input_format": "The first line contains n and the position where the tail connects. A value of -1 means no cycle.",
        "output_format": "Print YES if a cycle exists, otherwise print NO.",
        "constraints": "1 <= n <= 10^5.",
        "sample_input": "4 1\n3 2 0 -4",
        "sample_output": "YES"
    },

    {
        "title": "Search Insert Position",
        "description": "Given a sorted array and a target, return the index where the target is found or where it should be inserted.",
        "difficulty": "Easy",
        "input_format": "The first line contains n and target. The second line contains n sorted integers.",
        "output_format": "Print the required index.",
        "constraints": "1 <= n <= 10^5.",
        "sample_input": "4 5\n1 3 6 8",
        "sample_output": "2"
    },

    {
        "title": "Maximum Depth of Binary Tree",
        "description": "Given a binary tree, find its maximum depth.",
        "difficulty": "Medium",
        "input_format": "The first line contains n followed by the node values in level-order. Use -1 for a null node.",
        "output_format": "Print the maximum depth of the tree.",
        "constraints": "1 <= number of nodes <= 10^4.",
        "sample_input": "7\n3 9 20 -1 -1 15 7",
        "sample_output": "3"
    }
]


def seed_problems():
    db = SessionLocal()

    try:
        existing_count = db.query(Problem).count()

        if existing_count > 0:
            print(f"Problems already exist ({existing_count}).")
            return

        for problem_data in problems:
            problem = Problem(**problem_data)
            db.add(problem)

        db.commit()

        print(f"Successfully inserted {len(problems)} problems.")

    except Exception as e:
        db.rollback()
        print("Error while inserting problems:")
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_problems()