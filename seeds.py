from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
    User(username='abc', email='abc@email.abc', password='password123'),
    User(username='def', email='abc@email.def', password='password123'),
    User(username='ghi', email='abc@email.ghi', password='password123'),
    User(username='jkl', email='abc@email.jkl', password='password123'),
    User(username='mno', email='abc@email.mno', password='password123')
])