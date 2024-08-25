from flask import Blueprint, render_template

import podcast.adapters.repository as repo
from podcast.adapters.memory_repository import make_podcast_list_into_dict


description_blueprint = Blueprint(
    'description_bp', __name__)

@description_blueprint.route('/podcast_description/<podcast_title>', methods=['GET'])
def description(podcast_title):
    podcast_list = repo.repo_instance.get_podcast()
    podcast_dict = make_podcast_list_into_dict(podcast_list)
    return render_template(
        'description/description.html',
        podcast = podcast_dict[podcast_title]
    )