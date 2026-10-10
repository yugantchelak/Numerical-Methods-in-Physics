# How to collaborate...

## Making a local copy:

1. **Fork the repo first.** On the main page of the repo, https://github.com/yugantchelak/Numerical-Methods-in-Physics, CLICK the `Fork` button (top right). This makes your own copy of the repo under your GitHub account, which you are free to push to. ([GitHub's guide to forking](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo))

2. Clone **your fork** to your local machine. On the main page of your fork, CLICK the green `Code` button and copy the link. Then open a terminal or Git Bash and type:

```
$ git clone https://github.com/<YOUR-GITHUB-USERNAME>/Numerical-Methods-in-Physics.git
$ cd Numerical-Methods-in-Physics
```

3. Tell git where the original repo lives, so you can keep up to date with it. It's conventionally called `upstream`:

```
$ git remote add upstream https://github.com/yugantchelak/Numerical-Methods-in-Physics.git
```

**A note on passwords:** GitHub no longer accepts your account password for git over HTTPS. If git asks for a password when you push, use a **personal access token** instead ([how to create one](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)). Or, better, set up an **SSH key** once and never type anything again ([how to connect with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)). If you use SSH, clone with the `git@github.com:...` link from the `Code` button instead.

## Getting started

Now that you have a local copy of the repo, the following instructions will show you how to make changes.

4. Open up a new terminal/Git Bash on your machine and get the latest code from the original repo:

```
$ git checkout main
$ git pull upstream main
```

this will fetch all code from `upstream` and merge it into your local `main` branch.

5. Next we will make a branch for your work:

```
$ git checkout -b <YOUR-BRANCH-NAME>
```

this will create a new branch for you in which you can edit the files. Give it a name that says what you're doing, e.g. `fix-chapter-5-typos`.

6. Edit the files as you wish and add more files. Before committing a notebook, it's a good idea to restart the kernel and "Run All" to make sure it still runs from top to bottom.

7. Once you have finished adding and editing files, you need to stage your changes. Type the following command in your terminal:

```
$ git add <FILE 1> <FILE 2> ...
```

8. Then we need to write a commit message - describe what you did:

```
$ git commit -m "YOUR MESSAGE"
```

9. Push your branch to **your fork** (`origin`), not to the `main` branch:

```
$ git push origin <YOUR-BRANCH-NAME>
```

10. Go to your fork on GitHub. You'll see a button offering to open a **pull request** to the original repo. Click it, describe your changes and submit. ([GitHub's guide to pull requests from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork))

## USEFUL TIPS

- Always remember to pull from `upstream main` when you start working on a new bit.
- Also have fun!
