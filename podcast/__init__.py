"""Initialize Flask app."""
from flask import Flask, render_template
from podcast.adapters.datareader.csvdatareader import *
from podcast.adapters.memory_repository import MemoryRepository, populate

from podcast.domainmodel.model import *
import podcast.adapters.repository as repo

def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    #Don't remove this line of code
    #Any changes you make to the html it will show you those changes if u refresh the page
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    repo.repo_instance = MemoryRepository()
    populate(repo.repo_instance)

    with app.app_context():
        from podcast.Home import home
        app.register_blueprint(home.home_blueprint)

        from .description import description
        app.register_blueprint(description.description_blueprint)

        from .library import library
        app.register_blueprint(library.library_blueprint)



    # @app.route('/podcast_description/<int:podcast_id>')
    # def podcast_description(podcast_id):
    #     # Use Jinja to customize a predefined html page rendering the layout for showing a single podcast.
    #     podcast = CSVDataReader.podcast_list[podcast_id - 1]
    #     return render_template('home/description.html', podcast=podcast)
    #
    # @app.route('/')
    # def browse_page():
    #
    #     return render_template("home/home.html", podcasts=repo.repo_instance.get_podcast())

    return app
