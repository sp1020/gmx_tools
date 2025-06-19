#!/usr/bin/env bash

gmx grompp -f mdps_test/em.mdp -c ionized.gro -p topol.top -o em.tpr &&
    gmx mdrun -deffnm em -ntomp 8 &&
    gmx grompp -f mdps_test/nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr &&
    gmx mdrun -deffnm nvt -ntomp 8 &&
    gmx grompp -f mdps_test/npt.mdp -c nvt.gro -r em.gro -p topol.top -o npt.tpr &&
    gmx mdrun -deffnm npt -ntomp 8 &&
    gmx grompp -f mdps_test/md.mdp -c npt.gro -p topol.top -o md.tpr &&
    gmx mdrun -deffnm md -ntomp 8
