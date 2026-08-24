from collections import defaultdict


def analyze_weakness(submissions):
    """
    Analyze a user's submission history topic-wise.

    Returns:
        List of topic-wise performance and weakness information.
    """

    topic_stats = defaultdict(
        lambda: {
            "attempts": 0,
            "accepted": 0,
            "wrong_answer": 0,
            "time_limit_exceeded": 0,
            "runtime_error": 0,
            "compilation_error": 0
        }
    )

    for submission in submissions:
        if submission.status == "Pending":
            continue
        topic = submission.problem.topic

        if not topic:
            continue

        stats = topic_stats[topic]

        stats["attempts"] += 1

        if submission.status == "Accepted":
            stats["accepted"] += 1

        elif submission.status == "Wrong Answer":
            stats["wrong_answer"] += 1

        elif submission.status == "Time Limit Exceeded":
            stats["time_limit_exceeded"] += 1

        elif submission.status == "Runtime Error":
            stats["runtime_error"] += 1

        elif submission.status == "Compilation Error":
            stats["compilation_error"] += 1

    results = []

    for topic, stats in topic_stats.items():

        attempts = stats["attempts"]
        accepted = stats["accepted"]

        acceptance_rate = (
            (accepted / attempts) * 100
            if attempts > 0
            else 0
        )

        if acceptance_rate >= 70:
            weakness = "Strong"

        elif acceptance_rate >= 40:
            weakness = "Moderate"

        else:
            weakness = "Weak"

        results.append({
            "topic": topic,
            "attempts": attempts,
            "accepted": accepted,
            "wrong_answer": stats["wrong_answer"],
            "time_limit_exceeded": stats["time_limit_exceeded"],
            "runtime_error": stats["runtime_error"],
            "compilation_error": stats["compilation_error"],
            "acceptance_rate": round(acceptance_rate, 2),
            "weakness": weakness
        })

    results.sort(
        key=lambda x: x["acceptance_rate"]
    )

    return results