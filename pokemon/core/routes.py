from flask import Blueprint, render_template, request
from pokemon.models import Pokemon, Type, User
from pokemon.extensions import db

core_bp = Blueprint('core', __name__, template_folder='templates')

@core_bp.route('/')
def index():
  page = request.args.get('page',type=int)
  query = db.select(Pokemon)
  pokemons = db.paginate(query, page=page, per_page=4)
  return render_template('core/index.html',title='Home Page',pokemons=pokemons)

@core_bp.route('/<int:pokemon_id>/detail')
def pokemon_detail(pokemon_id):
  pokemon = db.session.get(Pokemon,pokemon_id)
  return render_template('core/pokemon_detail.html',title='Pokemon Detail Page',pokemon=pokemon)