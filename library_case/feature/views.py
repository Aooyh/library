
from . import features

@features.route('/hahha')
def hahha():
   from library_case.library_app import Author
   authors = Author.query.all()
   print(authors)

   return "fddfdfd"