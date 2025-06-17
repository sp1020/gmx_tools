# define box dimensions
docker run --rm  -u "$(id -u):$(id -g)" -v $(pwd):/app --workdir /app gromacs/gromacs ./script_md.sh
