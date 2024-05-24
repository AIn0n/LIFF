from argparse import ArgumentParser
import os


def main(proj_dir: str) -> None:
    routes = [
        (paths, filenames)
        for paths, _, filenames in os.walk(proj_dir)
        if "routes" in paths and "build" not in paths
    ]
    for route_dir, route_fn in routes:
        total_dir = os.path.join(route_dir, *route_fn)
        os.system(f"python3 {total_dir}")


if __name__ == "__main__":
    parser = ArgumentParser(prog="LIFF web framework")
    parser.add_argument("--path", "-p", help="path to the project folder", type=str)
    args = parser.parse_args()
    main(args.path)
