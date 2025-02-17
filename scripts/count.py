#!/bin/python

import json
import os
from pathlib import Path


def extract_type(fn, ctr):
    """function that reads metadata, extracts the type of package and adds it to a counter"""
    with open(fn, "r") as fh:
        t = json.load(fh).get("type", None)
        if t and t in ctr.keys():
            ctr[t] += 1


def main():
    root, folder, _ = next(os.walk("pkg"))
    ctr = {"lib": 0, "solver": 0, "app": 0, "data": 0}
    for fold in folder:
        metadata_path = Path(root) / fold / "metadata.json"
        if metadata_path.exists():
            extract_type(metadata_path, ctr)
    print(
        f"total: {len(ctr)} libs: {ctr['lib']} solver: {ctr['solver']} apps: {ctr['app']}, data: {ctr['data']}  "
    )


if __name__ == "__main__":
    main()
