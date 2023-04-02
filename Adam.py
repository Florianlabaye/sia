#test
from magic_admin import Magic

# Pass your API secret key directly to the Magic.
magic = Magic(api_secret_key='<YOUR_API_SECRET_KEY>')

# Or add an environment variable, `MAGIC_API_SECRET_KEY`
magic = Magic()
