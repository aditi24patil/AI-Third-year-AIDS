#Implement Greedy search algorithm for any of the following application:  
#Job Scheduling Problem 

def printJobScheduling(arr, max_deadline=None):
    n = len(arr)

    # Sort jobs according to profit in descending order
    arr.sort(key=lambda x: x[2], reverse=True)

    # If max_deadline is not specified, use the largest deadline from the job list
    if max_deadline is None:
        max_deadline = max(job[1] for job in arr)

    result = [False] * max_deadline  # Track free time slots
    job_sequence = ['None'] * max_deadline  # Store jobs assigned to slots

    # Assign jobs to the time slots
    for i in range(n):
        # Check from the latest possible slot for this job
        for j in range(min(max_deadline - 1, arr[i][1] - 1), -1, -1):
            if not result[j]:  # If slot is free
                result[j] = True
                job_sequence[j] = arr[i][0]  # Assign job ID to this slot
                break

    # Filter out unassigned slots from job_sequence for cleaner output
    assigned_jobs = [job_id for job_id in job_sequence if job_id != 'None']
    print("Job sequence for maximum profit:", assigned_jobs)

# Job format: [Job ID, Deadline, Profit]
jobs = [[1, 2, 50], [2, 1, 10], [3, 3, 40], [4, 2, 60], [5, 1, 30], [6, 3, 20]]
print("Following is the maximum profit sequence of jobs:")
printJobScheduling(jobs)
