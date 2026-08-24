from app.models import Problem, Submission


def get_recommendations(db, user_id: int, limit: int = 5):
    """
    Generate personalized problem recommendations.

    Priority:
    1. Problems from weak topics
    2. Problems the user has not solved
    3. Easier problems before harder ones
    """

    # Get all submissions made by the user
    submissions = (
        db.query(Submission)
        .filter(Submission.user_id == user_id)
        .all()
    )

    if not submissions:
        return []

    # Problems already solved successfully
    solved_problem_ids = {
        submission.problem_id
        for submission in submissions
        if submission.status == "Accepted"
    }

    # Calculate topic-wise performance
    topic_stats = {}

    for submission in submissions:
        if submission.status == "Pending":
            continue
        topic = submission.problem.topic

        if not topic:
            continue

        if topic not in topic_stats:
            topic_stats[topic] = {
                "attempts": 0,
                "accepted": 0
            }

        topic_stats[topic]["attempts"] += 1

        if submission.status == "Accepted":
            topic_stats[topic]["accepted"] += 1

    # Identify weak topics
    weak_topics = []

    for topic, stats in topic_stats.items():

        attempts = stats["attempts"]
        accepted = stats["accepted"]

        acceptance_rate = (
            accepted / attempts
            if attempts > 0
            else 0
        )

        if acceptance_rate < 0.70:
            weak_topics.append(topic)

    # Get all problems
    problems = (
        db.query(Problem)
        .order_by(Problem.id)
        .all()
    )

    recommendations = []

    difficulty_rank = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    for problem in problems:

        # Do not recommend already solved problems
        if problem.id in solved_problem_ids:
            continue

        score = 0
        reasons = []

        # Strong priority for weak topics
        if problem.topic in weak_topics:
            score += 100
            reasons.append(
                f"Recommended because {problem.topic} is a weak area"
            )

        # Prefer problems that the user has never attempted
        attempted = any(
            submission.problem_id == problem.id
            for submission in submissions
        )

        if not attempted:
            score += 30
            reasons.append("You have not attempted this problem yet")

        # Prefer easier problems
        score += (
            10 - difficulty_rank.get(
                problem.difficulty,
                2
            ) * 2
        )

        recommendations.append({
            "id": problem.id,
            "title": problem.title,
            "difficulty": problem.difficulty,
            "topic": problem.topic,
            "score": score,
            "reason": " • ".join(reasons)
        })

    # Highest recommendation score first
    recommendations.sort(
        key=lambda x: (
            -x["score"],
            difficulty_rank.get(
                x["difficulty"],
                2
            ),
            x["id"]
        )
    )

    return recommendations[:limit]