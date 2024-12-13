from app.controllers import get_post_controller

controller_modules = [get_post_controller]


def get_controllers():
    return controller_modules


def get_controller_routers():
    return [controller.router for controller in controller_modules]
