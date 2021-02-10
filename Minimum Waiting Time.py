# Minimum Waiting Time

# O(nlogn) time | O(1) space where n is the number of queries
# O(nlogn + n) cancels out to O(nlogn)
def minimumWaitingTime(queries):
    queries.sort()
    running_sum = 0
    prev_sum = 0
    for indx in range(len(queries) - 1):
        running_sum += queries[indx]
        prev_sum += running_sum

    return prev_sum


# O(nlogn) time | O(1) space where n is the number of queries
def minimumWaitingTime(queries):
    queries.sort()
    total_waiting_time = 0
    for idx, duration in enumerate(queries):
        queries_left = len(queries) - (idx + 1)
        total_waiting_time += duration * queries_left

    return total_waiting_time
