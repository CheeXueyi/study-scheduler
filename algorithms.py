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
        sub_det = [sub,random.randint(0,hrs_assigned)]
        subs.append(sub_det)
    return subs



#----Algorithms----

#Allocates number of half_hours for each subject with unallocated half_hours
def sub_hours(num_half_hours, subs):
    subs.sort(reverse=True,key=lambda x:x[1])
    i = 0
    while i < len(subs) and subs[i][1] != 0:
        num_half_hours-=subs[i][1]
        i+=1
    if len(subs)-i==0:
        return 0
    half_hours_per_remaining_sub = num_half_hours//(len(subs) - i)
    remaining_half_hours = num_half_hours % (len(subs)-i)
    for j in range(i,len(subs)):
        subs[j][1] += half_hours_per_remaining_sub
        if remaining_half_hours != 0:
            subs[j][1]+=1
            remaining_half_hours-=1

#breaks each subject n half_hour sessions where n is determined by the user, n can be 1,2,3 or 4
def study_session_breaker(subs,sess_len):
    sessions = []
    for i in subs:
        curr_sub = [i[0]]
        num_full_sess = i[1]//sess_len
        remaining_half_hrs = i[1]%sess_len
        curr_sub.extend([sess_len]*num_full_sess)
        if remaining_half_hrs != 0:
            curr_sub.append(remaining_half_hrs)
        sessions.append(curr_sub)
    return sessions
