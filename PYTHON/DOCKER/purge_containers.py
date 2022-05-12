#!/bin/env python

import os, sys

def get_containers():
    stream = os.popen('docker ps -a')
    data = stream.readlines()

    containers = []
    for i in range(1, len(data)):
        containers.append(data[i].split(" ")[0])


    return containers

def remove_containers(containers):
    if len(containers) < 1:
        print("There are no containers to remove")
        sys.exit(0)

    else:
        print(f"You are about to remove {len(containers)} container(s)!")
        answer = input("Are you sure? [y/n]: ")

        if answer in ['y', 'Y', 'yes', 'YES']:
            for c in containers:
                os.popen('docker container rm '+c)
            print("Containers were successfully removed!")
            sys.exit(0)
        else:
            print("Operation aborted by user!")
            sys.exit(0)

def main():
    containers = get_containers()
    remove_containers(containers)


if __name__ == "__main__":
    main()
