from flask import Blueprint, render_template, request

import podcast.adapters.repository as repo


library_blueprint = Blueprint('library_bp', __name__)

@library_blueprint.route('/library', methods=['GET'])
def library():

    podcasts = repo.repo_instance.get_podcast()


    page = request.args.get('page', 1, type=int)
    per_page = 30
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(podcasts) + per_page - 1) // per_page

    podcasts_on_page = podcasts[start:end]


    return render_template(
        'library/library.html',
        podcasts_on_page=podcasts_on_page,
        total_pages=total_pages,
        page=page
    )