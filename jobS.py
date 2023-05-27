def find_slot(slot, deadline):
    for i in range(deadline - 1, -1, -1):
        if not slot[i]:
            return i
    return -1



def job_scheduling(sorted_jobs):
    n = len(sorted_jobs)
    # sorted_jobs = [[i, jobs[i][0], jobs[i][1]] for i in range(n)]
    # sorted_jobs.sort(key=lambda i: i[2])           
    sorted_jobs.sort(key=lambda i: i[2])

    schedule = []
    profit = 0
    slot = [False] * n

    for i in range(n - 1, -1, -1):
        deadline = sorted_jobs[i][1]
        index = find_slot(slot, deadline)

        if index != -1:
            slot[index] = True
            schedule.append(sorted_jobs[i][0])
            profit += sorted_jobs[i][2]
    print("ID   Deadline  Profit")
    for i in range (n-1,-1,-1):
        print(sorted_jobs[i][0] ,"   ",sorted_jobs[i][1],"      ",sorted_jobs[i][2])
    print("Scheduled jobs:")
    for jobId in schedule:
        print("Job", jobId)

    print("Total profit:", profit)


jobs = [[0,2, 30], [1,1, 30], [2,1, 70], [3,2, 90], [4,3, 30]]
job_scheduling(jobs)


