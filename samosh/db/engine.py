import os
import dotenv
dotenv.load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

import sqlalchemy as db
engine = db.create_engine(DATABASE_URL)