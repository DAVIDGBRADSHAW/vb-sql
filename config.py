import os

# For production: use secret key:
# To generate:
# python -c "import secrets;print(secrets.token_hex())"

#postgresql://sqldatabase_3tep_user:N3ijN7fUVlfPBJwtEPbQfQQMR5dnP5Hp@dpg-craes6l6l47c73dbblk0-a.frankfurt-postgres.render.com/sqldatabase_3tep

#postgresql://sqldatabase_3tep_user:
# N3ijN7fUVlfPBJwtEPbQfQQMR5dnP5Hp
# @dpg-craes6l6l47c73dbblk0-a.frankfurt-postgres.render.com
# /sqldatabase_3tep
SECRET_KEY = os.getenv('SECRET_KEY', 'replace with generated key here')

SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

"""
#WAY2:
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:///project.db")

## BETTER:
## Get from ENV variable or revert to connection string as default
"""