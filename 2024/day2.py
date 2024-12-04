reports = []

with open('day2_input.txt') as file:
    for line in file:
        reports.append([int(i) for i in line.split(" ")])

def safe(report):
    # this variable is True when report is 'supposed' to be increasing
    # and False when report is 'supposed' to be decreasing
    dir = (report[-1]-report[0]) > 0
    for i in range(len(report)-1):
        # ok so how do we define unsafe
        # either wrong direction or too much distance
        # find direction at start?
        new_dir = (report[i+1]-report[i]) > 0
        if ( (new_dir!=dir) or 
            not(1 <= abs(report[i+1]-report[i]) <= 3)
            ):
            return False 
    else:
        return True
    
print("part 1")
print([safe(report) for report in reports].count(True))

def safe_modified(report):
    return safe_mod_helper(report, 0)

# this function just checks whether any array is valid or not   
def safe_mod_helper(report, count):    

    dir = (report[-1]-report[0]) > 0

    for i in range(len(report)-1):
        new_dir = (report[i+1]-report[i]) > 0
        if ( (new_dir!=dir) or 
            not(1 <= abs(report[i+1]-report[i]) <= 3)
            ):
            if (count==1):
                return False
            else:
                timeline1 = [report[j] for j in range(len(report)) if j!=i]
                timeline2 = [report[j] for j in range(len(report)) if j!=i+1]
                return safe_mod_helper(timeline1, 1) or safe_mod_helper(timeline2, 1)
    else:
        return True


# results = [safe_modified(report) for report in reports]

# for i in range(len(results)):
#     if not(results[i]):
#         print("===")
#         print(reports[i])
#         print(results[i])

print("part 2")
print([safe_modified(report) for report in reports].count(True))