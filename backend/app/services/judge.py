from app.services.cpp_executor import execute_cpp_code


def normalize_output(output: str) -> str:
    """
    Normalize harmless whitespace differences.
    """
    return " ".join(output.strip().split())


def judge_submission(
    code: str,
    test_cases: list,
    time_limit: int = 3
):
    """
    Judge a C++ submission using OnlineCompiler.io.

    time_limit is the CodeForge time limit per test case,
    in seconds.
    """

    total_execution_time = 0

    for test_case in test_cases:

        result = execute_cpp_code(
            code=code,
            input_data=test_case.input_data,
            timeout=30
        )

        execution_time = result.get(
            "execution_time", 0
        )

        total_execution_time += execution_time

        # Compiler / runtime / OnlineCompiler error
        if result["status"] != "Executed":
            return {
                "status": result["status"],
                "output": result["output"],
                "error": result["error"],
                "execution_time": total_execution_time
            }

        # CodeForge time limit
        if execution_time > time_limit * 1000:
            return {
                "status": "Time Limit Exceeded",
                "output": result["output"],
                "error": (
                    f"Time limit of {time_limit} seconds exceeded."
                ),
                "execution_time": total_execution_time
            }

        actual_output = normalize_output(
            result["output"]
        )

        expected_output = normalize_output(
            test_case.expected_output
        )

        # Wrong answer
        if actual_output != expected_output:
            return {
                "status": "Wrong Answer",
                "output": result["output"],
                "error": "",
                "execution_time": total_execution_time
            }

    # All test cases passed
    return {
        "status": "Accepted",
        "output": "",
        "error": "",
        "execution_time": total_execution_time
    }