from sqlalchemy import create_engine
import os

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

print(os.path.abspath("data/db/bluestock_mf.db"))

with engine.connect() as conn:
    print("Database connected successfully!")