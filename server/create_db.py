from database import Base,engine

# Create the database
Base.metadata.create_all(engine)