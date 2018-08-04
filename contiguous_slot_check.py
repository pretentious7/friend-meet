
import queue
import datetime


def slot_check(persons):
    i = earliest_time(persons)
    maxslot = datetime.timedelta(minutes=15)
    startmax = 0
    endmax = 0



    len_list = queue.PriorityQueue()
    while i<=latest_time(persons):
        slotlen = datetime.timedelta(minutes=0)
        while all_slots_free(i,persons):
            slotlen = increment_time(slotlen)
            i = increment_time(i)
        if slotlen>datetime.timedelta(minutes=1):
            len_list.put((-slotlen,i-slotlen))
        if slotlen>maxslot:
            startmax = i-slotlen
            endmax = i
            maxslot = slotlen

        i = increment_time(i)

    print(startmax,endmax)
    while len_list.empty() is False:
        print(-len_list.get()[0])
        print('ola')
    return (startmax,endmax)



def free_slot(person, timeno):
    #timeno = datetime.datetime(year=1,month=1,day=1,minute=timeno)
    if timeno in person.schedule.times:
        return True
    else:
        return False


def all_slots_free(time_moment,person_list):
    slotfree = True
    for i in person_list:
        if free_slot(i,time_moment) is False:
            slotfree = False

    print(slotfree)


    return slotfree


def increment_time(time_moment):
    return time_moment + datetime.timedelta(minutes=30)


def earliest_time(person_list):
    """
    note that this won't work after the year 3000.
    :param person_list:
    :return:
    """
    early_time = datetime.datetime(year=3000,month=1,day=1,minute=0)
    for i in person_list:
        for time in i.schedule.times:
            if time<early_time:
                early_time = time

    return early_time


def latest_time(person_list):
    late_time = datetime.datetime(year=1,month=1,day=1,minute=0)
    for i in person_list:
        for time in i.schedule.times:
            if time>late_time:
                late_time = time

    return late_time
