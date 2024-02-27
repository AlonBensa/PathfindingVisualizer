from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# uvicorn main:app --reload

origins = [
    "http://localhost",
    "http://localhost:3000",  # Update with the actual frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

from Generator.BinaryTreeAlgorithm import BinaryTreeAlgorithm
from Solver.Bfs import Bfs
from Solver.Dfs import Dfs
from Solver.Dijkstra import Dijkstra
from Solver.Astar import Astar

app.include_router(BinaryTreeAlgorithm().router, prefix="/Generator", tags=["Generator Algorithms"])
app.include_router(Bfs().router, prefix="/Solver", tags=["Solving Algorithms"])
app.include_router(Dfs().router, prefix="/Solver", tags=["Solving Algorithms"])
app.include_router(Dijkstra().router, prefix="/Solver", tags=["Solving Algorithms"])
app.include_router(Astar().router, prefix="/Solver", tags=["Solving Algorithms"])
