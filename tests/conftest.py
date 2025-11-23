import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base, get_session
from src.main import app
from src.models import *


SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

app.dependency_overrides[get_session] = override_get_session


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def sample_movies():
    session = TestingSessionLocal()
    movies = [
        Movie(title="Movie 1", genres="Action"),
        Movie(title="Movie 2", genres="Comedy"),
        Movie(title="Movie 3", genres="Drama")
    ]
    session.add_all(movies)
    session.commit()

    for m in movies:
        session.refresh(m)
    yield movies

    for m in movies:
        session.delete(m)
    session.commit()
