from fastapi import FastAPI
from app.controllers import get_post_controller
from app.core.di import get_controller_routers
from app.core.container import Container, wire_controllers

app = FastAPI()

# TODO: the command of uvicorn is "uvicorn app.core.main:app --reload". I am running this in the directory where main.py is located.

routers = get_controller_routers()

for router in routers:
    app.include_router(router)


container = Container()
wire_controllers(container)
app.container = container

# run fastapi server using "python main.py"
# uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
