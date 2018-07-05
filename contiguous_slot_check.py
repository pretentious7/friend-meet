
import queue

def slot_check(persons):
    i = 0
    maxslot = 0
    startmax = 0
    endmax = 0

    len_list = queue.PriorityQueue()
    while i<24*2*7:
        slotlen = 0
        while all_slots_free(i,persons):
            slotlen+=1
            i+=1
        if slotlen>0:
            len_list.put((-slotlen,i-slotlen))
        if slotlen>maxslot:
            startmax = i-slotlen
            endmax = i
            maxslot = slotlen

        i+=1
        print(i)

    print(startmax,endmax)
    while len_list.empty() is False:
        print(len_list.get())



def free_slot(person, timeno):
    if timeno in person.schedule.times:
        return True
    else:
        return False


def all_slots_free(time_moment,person_list):
    slotfree = True
    for i in person_list:
        if free_slot(i,time_moment) is False:
            slotfree = False


    return slotfree

