from apistar import App
from project.routes import routes
from project.models import Base
from apistar.commands import create_tables

settings = {
    "DATABASE": {
	    "URL": "sqlite:///db.sqlite3",
            "METADATA": Base.metadata
    }
}
app = App(routes=routes, settings=settings)
app = App(routes=routes, settings=settings, commands=[create_tables])
if __name__ == "__main__":
    app.click()