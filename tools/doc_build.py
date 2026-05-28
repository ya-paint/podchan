import subprocess
import os
import sys

def run_apidoc():
    docs_dir = os.path.join(os.path.dirname(__file__), "..", "docs")

    cmd = [
        "sphinx-apidoc",
        "-f",
        "-o",
        "source/class",
        "../src"
    ]

    print("Running sphinx-apidoc...")
    result = subprocess.run(cmd, cwd=docs_dir)

    if result.returncode != 0:
        print("sphinx-apidoc failed")
        sys.exit(1)


def build_html():
    docs_dir = os.path.join(os.path.dirname(__file__), "..", "docs")

    print("Building HTML...")
    result = subprocess.run(
        ["make", "html"],
        cwd=docs_dir
    )

    if result.returncode != 0:
        print("Sphinx build failed")
        sys.exit(1)


def main():
    run_apidoc()
    build_html()
    print("Docs build complete")


if __name__ == "__main__":
    main()