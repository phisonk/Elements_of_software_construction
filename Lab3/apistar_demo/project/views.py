
from apistar.backends import SQLAlchemy
from .models import Poll, Choice

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def students():
    aStudentT = {'id': '59011604', 'firstname': 'phison', 'lastname': 'khankhang'}
    aStudent = [{'id': '59011597', 'firstname': 'Chatchanok', 'lastname': 'Wongsamang'},
{'id': '59011598', 'firstname': 'Jiramate', 'lastname': 'Leingprom'},
{'id': '59011599', 'firstname': 'Jirayu', 'lastname': 'Promsongwong'},
{'id': '59011600', 'firstname': 'Kitpol', 'lastname': 'Tansakul'},
{'id': '59011601', 'firstname': 'Nattamon', 'lastname': 'Sridam'},
{'id': '59011602', 'firstname': 'Peeranat', 'lastname': 'Limpitaporn'},
{'id': '59011604', 'firstname': 'Phison', 'lastname': 'Khankang'},
{'id': '59011605', 'firstname': 'Thirawat', 'lastname': 'Rungrotchaiyaporn'}]
    return aStudent

allStudent = students()
def students_get(aindex):
    for i in allStudent:
        if aindex == i['id']:
            print('yeah')
            return i
            break

def create_poll(db: SQLAlchemy, question: str):
    session = db.session_class()
    poll = Poll(question=question)
    session.add(poll)
    session.commit()
    return {'question': question}


def create_choices(db: SQLAlchemy, poll_id: int, choice_text: str):
    session = db.session_class()
    poll = session.query(Poll).get(poll_id)
    choice = Choice(poll=poll.id, choice_text=choice_text, votes=0)
    session.add(choice)
    session.commit()
    return {'choice_text': choice_text}
