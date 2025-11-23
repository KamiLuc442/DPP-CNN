from fastapi import FastAPI
from .movies.router import router as movies_router
from .links.router import router as links_router
from .ratings.router import router as ratings_router
from .tags.router import router as tags_router
from .auth.router import router as auth_router

app = FastAPI()
app.include_router(movies_router)
app.include_router(links_router)
app.include_router(ratings_router)
app.include_router(tags_router)
app.include_router(auth_router)
