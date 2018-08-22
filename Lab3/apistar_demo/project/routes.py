from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome , students,students_get
from project.views import  create_poll, create_choices



routes = [
    Route('/students/id/{aindex}','GET',students_get),
    Route('/students','GET',students),
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes),
    # API to create Polls
    Route('/create_poll', 'POST', create_poll),
    # API to add choices to the polls
    Route('/create_choices', 'POST', create_choices),
]
