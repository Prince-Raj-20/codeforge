import requests
import time

from app.config import settings


ONLINE_COMPILER_URL = (
    "https://api.onlinecompiler.io/api/run-code-sync/"
)


def sanitize_compiler_error(error: str) -> str:
    """
    Return a clean compiler error message.
    """
    if not error:
        return ""

    return error.strip()


def execute_cpp_code(
    code: str,
    input_data: str,
    executable_path=None,
    temp_dir=None,
    timeout: int = 3,
    cleanup: bool = True
):
    """
    Execute C++17 code using OnlineCompiler.io.
    """

    start_time = time.perf_counter()

    try:
        response = requests.post(
            ONLINE_COMPILER_URL,
            headers={
                "Authorization": settings.ONLINECOMPILER_API_KEY,
                "Content-Type": "application/json"
            },
            json={
                "compiler": "g++-15",
                "code": code,
                "input": input_data
            },
            timeout=35
        )

        execution_time = int(
            (time.perf_counter() - start_time) * 1000
        )

        # OnlineCompiler HTTP/API failure
        if response.status_code != 200:
            return {
                "status": "Execution Error",
                "output": "",
                "error": (
                    f"OnlineCompiler API error "
                    f"({response.status_code})"
                ),
                "execution_time": execution_time,
                "executable_path": None,
                "temp_dir": None
            }

        result = response.json()

        output = result.get("output", "")
        error = result.get("error", "")
        api_status = result.get("status", "")
        exit_code = result.get("exit_code")

        # Successful execution
        if api_status == "success" and exit_code == 0:
            return {
                "status": "Executed",
                "output": output,
                "error": "",
                "execution_time": execution_time,
                "executable_path": None,
                "temp_dir": None
            }

        # OnlineCompiler execution timeout
        if exit_code == 124:
            return {
                "status": "Time Limit Exceeded",
                "output": output,
                "error": "Execution timed out.",
                "execution_time": execution_time,
                "executable_path": None,
                "temp_dir": None
            }

        # Program crashed / runtime failure
        if exit_code == -1:
            return {
                "status": "Runtime Error",
                "output": output,
                "error": "Program terminated with a runtime error.",
                "execution_time": execution_time,
                "executable_path": None,
                "temp_dir": None
            }

        # Compiler error
        if error:
            return {
                "status": "Compilation Error",
                "output": output,
                "error": sanitize_compiler_error(error),
                "execution_time": execution_time,
                "executable_path": None,
                "temp_dir": None
            }

        # Unknown execution failure
        return {
            "status": "Execution Error",
            "output": output,
            "error": "Code execution failed.",
            "execution_time": execution_time,
            "executable_path": None,
            "temp_dir": None
        }

    except requests.Timeout:
        return {
            "status": "Execution Error",
            "output": "",
            "error": "OnlineCompiler request timed out.",
            "execution_time": int(
                (time.perf_counter() - start_time) * 1000
            ),
            "executable_path": None,
            "temp_dir": None
        }

    except requests.RequestException:
        return {
            "status": "Execution Error",
            "output": "",
            "error": "Unable to reach OnlineCompiler.",
            "execution_time": int(
                (time.perf_counter() - start_time) * 1000
            ),
            "executable_path": None,
            "temp_dir": None
        }

    except Exception:
        return {
            "status": "Execution Error",
            "output": "",
            "error": "An internal execution error occurred.",
            "execution_time": int(
                (time.perf_counter() - start_time) * 1000
            ),
            "executable_path": None,
            "temp_dir": None
        }