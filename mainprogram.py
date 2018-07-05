from person import *
from contiguous_slot_check import *

print('ojuu')
timedef = list(range(24*14)[0:30])
print(timedef)

ojas = Person()
abhishek = Person()

ojas.schedule.addtime(32)
ojas.schedule.addtime(12)
ojas.schedule.addtime(13)

abhishek.schedule.addtime(12)
abhishek.schedule.addtime(32)
abhishek.schedule.addtime(13)

ananya = Person()
ananya.schedule.addtime(13)
ananya.schedule.addtime(32)
ananya.schedule.addtime(12)
print(ojas.schedule.times)

personages = [ojas,abhishek,ananya]
slot_check(personages)