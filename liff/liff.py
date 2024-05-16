from itertools import tee
import inspect, os


def get_caller_script_path():
    # Get the call stack
    stack = inspect.stack()

    # Traverse the stack until we find the first frame
    # that doesn't belong to the module itself
    for frame_info in stack:
        frame = frame_info.frame
        filename = frame.f_code.co_filename
        if filename != __file__:
            return filename

    # Return None if we couldn't find the caller script
    return None


def get_project_route_script_path():
    *path_parts, script = get_caller_script_path().split("/")
    project, routes = [], []
    routes_detected = False
    for part in path_parts:
        if part == "routes":
            routes_detected = True
            continue
        (project, routes)[routes_detected].append(part)

    return map(lambda x: "/".join(x), (project, routes, [script]))


def change_extension(path: str, new_ext: str) -> str:
    curr_path, curr_ext = path.split(".")
    return f"{curr_path}.{new_ext}"


def page(code: str) -> None:
    project, route, script = get_project_route_script_path()
    build = f"{project}/build/routes/{route}"
    if not os.path.exists(build):
        os.makedirs(build)
    with open(build + change_extension(script, "html"), "wt") as file:
        print(code, file=file)


def center(children=None):
    code = '<div style="display: flex; flex-direction: column; align-items: center; background-color: lightblue;">'
    for child in children:
        code += child
    code += "</div>"
    return code


def text(string: str):
    return f"<p> {string} </p>"


def button(child=None, action=None):
    if not action:
        return f"<button>{child}</button>"
    action = f"'{action}'"
    return f'<button onclick="window.location.href={action}">{child}</button>'


def goto(path: str):
    return path
