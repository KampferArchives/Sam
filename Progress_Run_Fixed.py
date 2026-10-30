"""SAM — FIXED VERSION: includes every 1-based session endpoint."""


def best_progress_run(values):
    best_total = values[0]

    for start_index in range(len(values)):
        running_total = 0
        start_session = start_index + 1

        for end_session in range(start_session, len(values) + 1):
            running_total += values[end_session - 1]
            best_total = max(best_total, running_total)

    return best_total


if __name__ == "__main__":
    progress = [-4, 3, -2, 5]
    print(best_progress_run(progress))  # 6, from [3, -2, 5]
