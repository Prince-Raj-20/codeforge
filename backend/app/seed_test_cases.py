# seed_test_cases.py

from app.database import SessionLocal
from app.models import Problem, TestCase


test_cases = {
    "Two Sum": [
        ("4 9\n2 7 11 15", "0 1", True),
        ("5 10\n1 3 7 8 11", "1 3", True),
        ("2 6\n1 5", "0 1", False),
        ("6 13\n4 9 2 11 7 6", "0 1", False),
        ("5 0\n-3 1 4 -1 3", "0 4", False),
    ],

    "Maximum Subarray": [
        ("9\n-2 1 -3 4 -1 2 1 -5 4", "6", True),
        ("5\n1 2 3 4 5", "15", True),
        ("4\n-5 -2 -8 -1", "-1", False),
        ("6\n-2 5 -1 7 -3 4", "12", False),
        ("8\n3 -2 5 -1 6 -4 2 1", "11", False),
    ],

    "Palindrome Number": [
        ("121", "YES", True),
        ("-121", "NO", True),
        ("12321", "YES", False),
        ("123456", "NO", False),
        ("10", "NO", False),
    ],

    "House Robber": [
        ("5\n2 7 9 3 1", "12", True),
        ("4\n1 2 3 1", "4", True),
        ("6\n10 1 1 10 1 1", "21", False),
        ("8\n2 7 9 3 1 5 8 4", "24", False),
        ("5\n5 1 1 5 1", "10", False),
    ],

    "Valid Parentheses": [
        ("({[]})", "YES", True),
        ("([)]", "NO", True),
        ("((()))", "YES", False),
        ("{[()()]}", "YES", False),
        ("((]", "NO", False),
    ],

    "Best Time to Buy and Sell Stock": [
        ("5\n7 1 5 3 6", "5", True),
        ("5\n7 6 4 3 1", "0", True),
        ("6\n2 4 1 8 3 10", "9", False),
        ("7\n10 2 5 1 9 4 12", "11", False),
        ("4\n1 2 3 4", "3", False),
    ],

    "Number of Islands": [
        ("4 5\n11000\n11000\n00100\n00011", "3", True),
        ("3 3\n111\n010\n111", "1", True),
        ("5 5\n10000\n00100\n00010\n00001\n00000", "4", False),
        ("4 4\n1111\n0000\n1111\n0000", "2", False),
        ("3 5\n10001\n00100\n10001", "5", False),
    ],

    "Binary Search": [
        ("6 9\n1 3 5 7 9 11", "4", True),
        ("5 4\n1 2 4 5 6", "-1", True),
        ("7 1\n1 2 3 4 5 6 7", "0", False),
        ("8 15\n2 4 6 8 10 12 14 15", "7", False),
        ("5 -3\n-10 -5 -3 0 4", "2", False),
    ],

    "Longest Substring Without Repeating Characters": [
        ("abcabcbb", "3", True),
        ("bbbbb", "1", True),
        ("pwwkew", "3", False),
        ("abcdefg", "7", False),
        ("abba", "2", False),
    ],

    "Move Zeroes": [
        ("5\n0 1 0 3 12", "1 3 12 0 0", True),
        ("3\n0 0 1", "1 0 0", True),
        ("6\n1 2 3 4 5 6", "1 2 3 4 5 6", False),
        ("7\n0 4 0 0 5 0 2", "4 5 2 0 0 0 0", False),
        ("5\n0 0 0 0 0", "0 0 0 0 0", False),
    ],

    "Reverse Integer": [
        ("123", "321", True),
        ("-123", "-321", True),
        ("120", "21", False),
        ("1534236469", "0", False),
        ("-2147483648", "0", False),
    ],

    "Container With Most Water": [
        ("9\n1 8 6 2 5 4 8 3 7", "49", True),
        ("2\n1 1", "1", True),
        ("5\n1 2 4 3 5", "12", False),
        ("6\n5 4 3 2 1 5", "25", False),
        ("7\n2 3 10 5 7 8 9", "45", False),
    ],

    "Valid Anagram": [
        ("listen\nsilent", "YES", True),
        ("rat\ncar", "NO", True),
        ("anagram\nnagaram", "YES", False),
        ("hello\nworld", "NO", False),
        ("aabbcc\nabcabc", "YES", False),
    ],

    "Merge Sorted Array": [
        ("3 3\n1 2 4\n1 3 5", "1 1 2 3 4 5", True),
        ("3 2\n1 3 5\n2 4", "1 2 3 4 5", True),
        ("4 3\n1 4 7 9\n2 3 8", "1 2 3 4 7 8 9", False),
        ("2 4\n5 10\n1 2 3 4", "1 2 3 4 5 10", False),
        ("3 3\n-5 0 8\n-4 1 7", "-5 -4 0 1 7 8", False),
    ],

    "Climbing Stairs": [
        ("5", "8", True),
        ("2", "2", True),
        ("10", "89", False),
        ("20", "10946", False),
        ("30", "1346269", False),
    ],

    "Reverse Linked List": [
        ("5\n1 2 3 4 5", "5 4 3 2 1", True),
        ("3\n1 2 3", "3 2 1", True),
        ("1\n42", "42", False),
        ("7\n10 20 30 40 50 60 70", "70 60 50 40 30 20 10", False),
        ("6\n-3 0 5 8 -2 9", "9 -2 8 5 0 -3", False),
    ],

    "First Unique Character": [
        ("leetcode", "0", True),
        ("aabb", "-1", True),
        ("loveleetcode", "2", False),
        ("abcabcx", "6", False),
        ("aabbccd", "6", False),
    ],

    "Linked List Cycle": [
        ("4 1\n3 2 0 -4", "YES", True),
        ("4 -1\n1 2 3 4", "NO", True),
        ("5 0\n1 2 3 4 5", "YES", False),
        ("6 3\n10 20 30 40 50 60", "YES", False),
        ("3 -1\n5 6 7", "NO", False),
    ],

    "Search Insert Position": [
        ("4 5\n1 3 6 8", "2", True),
        ("4 2\n1 3 5 6", "1", True),
        ("5 10\n1 3 5 7 9", "5", False),
        ("6 0\n1 2 3 4 5 6", "0", False),
        ("5 6\n1 2 4 6 8", "3", False),
    ],

    "Maximum Depth of Binary Tree": [
        ("7\n3 9 20 -1 -1 15 7", "3", True),
        ("3\n1 2 3", "2", True),
        ("1\n1", "1", False),
        ("7\n1 2 3 4 5 6 7", "3", False),
        ("5\n1 2 -1 3 -1", "3", False),
    ],
}


def seed_test_cases():
    db = SessionLocal()

    try:
        existing_count = db.query(TestCase).count()

        if existing_count > 0:
            print(f"Test cases already exist ({existing_count}).")
            return

        total_inserted = 0

        for title, cases in test_cases.items():

            problem = (
                db.query(Problem)
                .filter(Problem.title == title)
                .first()
            )

            if not problem:
                print(f"Problem not found: {title}")
                continue

            for input_data, expected_output, is_public in cases:

                test_case = TestCase(
                    problem_id=problem.id,
                    input_data=input_data,
                    expected_output=expected_output,
                    is_public=is_public,
                )

                db.add(test_case)
                total_inserted += 1

        db.commit()

        print(f"Successfully inserted {total_inserted} test cases.")

    except Exception as e:
        db.rollback()
        print("Error while inserting test cases:")
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_test_cases()