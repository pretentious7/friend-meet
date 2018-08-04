from person import *
from contiguous_slot_check import *
from flask import Flask,render_template,request,session
from flask_session import Session
import datetime
from datetime import datetime
import uuid
import pandas

"""
TODO:
1. add earliest and latest time tracker for algo period determination.

"""
app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"

Session(app)

Usertimes = []
@app.route("/",methods= ["GET","POST"])
def index():
    """
    Main index of webpage at route /, shows time entry
    :return:
    """


    if session.get('u') is None:
        session["u"] = uuid.uuid4()



    session['persons'] = []
    print(session['u'])

    return render_template("index.html", u=session['u'])


@app.route("/stuff",methods=["POST"])
def stuff():


    time = request.form.get("time")
    print(time)
    print('ojuu')
    time = datetime.fromisoformat(str(time))
    time = time.replace(tzinfo=None)
    name = request.form.get("name")


    if session.get(name) is None:
        session[name] = Person(name = name)
        session['persons'].append(session[name])
    session[name].schedule.addtime(time)
    if session.get('session_db') is None:
        session['session_db'] = pandas.DataFrame({'times': pandas.Timestamp(time),
                                                  'name':name},index=[0])
    else:
        session['session_db'].append([time,name])
        print(session['session_db'])

    return render_template("index.html",time=time,userface = session[name].schedule.times,persons = [person.name for person in session['persons']],
                           timelist = slot_check(session['persons']))


@app.route("/time")
def time():
    return None


@app.route('/<uuid:u>')
def new_person(u=1):
    return f"{u}"



'''
print('ojuu')
timedef = list(range(24*14)[0:30])
print(timedef)

ojas = Person()
abhishek = Person()

ojas.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=2,minute=0))
ojas.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=2,minute=30))
ojas.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=3,minute=0))
ojas.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=4,minute=0))

abhishek.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=2,minute=0))
abhishek.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=2,minute=30))
abhishek.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=3,minute=0))
abhishek.schedule.addtime(datetime.datetime(year=2,month=2,day=1,hour=4,minute=0))


#ananya = Person()
#ananya.schedule.addtime(13)
#ananya.schedule.addtime(32)
#ananya.schedule.addtime(12)
print(ojas.schedule.times)

personages = [ojas,abhishek]
slot_check(personages)

'''