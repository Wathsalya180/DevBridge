from sqlalchemy.orm import sessionmaker, Session

from app.core.database import engine


# Create a factory for database sessions
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# Provide a database session to API endpoints
def get_db():
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()
