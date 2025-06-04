# python_app_template
A template for Python package

### Step 1. Clone the template 

The template will be cloned into the directory of a new project, and the `.git` directory will be deleted. 

```
git clone git@github.com:sp1020/python_app_template.git ./NEW_PROJECT
cd NEW_PROJECT
rm .git -rf
```

### Step 2. Create a new repository in GitHub

1. Create a new repository in GitHub (NEW_PROJECT).
1. Then clone the repository in the NEW_PROJECT directory

```
cd NEW_PROJECT
git init 
git add .
git commit -m "application template"
git branch -M main
git remote add origin git@github.com:sp1020/NEW_PROJECT.git
git push -u origin main
```

### (Alternative) Step 2. Create a new repository in other server 

1. Create a new repository in the Git repository server. )

```
mkdir NEW_PROJECT.git
cd NEW_PROJECT.git
git init --bare
```

2. Create a new git repository in the analysis server

```
cd NEW_PROJECT
git init
git add .
git commit -m "a new application"
```

3. Connect the analysis git repository to server repository

```
git remote add origin ssh://sp1020@GIT_SERVER:/home/sp1020/git_repository/NEW_PROJECT.git
git push origin master
```


