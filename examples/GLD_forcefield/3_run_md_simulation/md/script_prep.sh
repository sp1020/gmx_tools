#!/usr/bin/env bash

# define box dimensions
gmx pdb2gmx -f input/cleaned.pdb -o processed.gro -p topol.top -ff charmm36 -water tip3p
    gmx editconf -f processed.gro -o boxed.gro -c -d 1.0 -bt dodecahedron &&
    gmx solvate -cp boxed.gro -cs spc216.gro -o solvated.gro -p topol.top &&
    gmx grompp -f mdps/ions.mdp -c solvated.gro -p topol.top -o ions.tpr -maxwarn 1 &&
    echo SOL | gmx genion -s ions.tpr -p topol.top -o ionized.gro -pname NA -nname CL -neutral
