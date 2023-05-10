import random

#----dummy data generators----

#returns a list of "day detail"s, 1 represents selected, 0 represents not selected random list of 1s and 0s 
def dummy_hours():
    hrs = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    for i in hrs:
        for _ in range(48):
            i.append(random.randint(0,1))
    return hrs

#returns a list of subs where each element is (subject, hours). if hours = 0, then hours for this subject has not been manually set.
def dummy_subjects(half_hours):
    sub_list = ["History", "Math", "Chemistry", "Physics", "English", "Data Structures", "Geography","Music", "Economics","Finance","Business"]
    subs = []
    num_subs = random.randint(1,10)
    subs_sbset = random.sample(sub_list,num_subs)
    for sub in subs_sbset:
        hrs_assigned = random.randint(0,half_hours)
        half_hours -= hrs_assigned
        sub_det = (sub,random.randint(0,hrs_assigned))
        subs.append(sub_det)
    return subs
