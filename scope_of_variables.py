#!/usr/bin/env python3
# Created by: Marli Peters
# Created on: Oct. 2, 2023
# This module shows how local and global variables work.

# global variable
variable_x = 20


def local_variable() -> None:
    variable_x = 16
    variable_y = 32

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Local variable:  {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    global variable_x
    variable_y = 48

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()
