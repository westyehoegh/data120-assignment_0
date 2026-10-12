# Assignment 0 — Tools Bootcamp

**Points:** 0 (optional, but strongly recommended)

## Why we’re doing this

This assignment is **not required for course credit** and is worth **0 points**.

However:

> If you do **not** complete this practice assignment, you are **not eligible for leniency or extensions** on future assignments due to **technical issues** such as Git/GitHub problems, Gradescope submission issues, or local environment setup problems.

The goal is to make sure you have practiced the full course workflow **before it counts for a grade**.

## Learning goals

By the end of this assignment, you will be able to:

- Verify that Python, VS Code, Git, and GitHub are set up correctly
- Create a GitHub account, if needed
- Accept a course repository and get your own copy
- Clone a repository and work locally
- Create a branch, commit changes, and push them to GitHub
- Open and merge a Pull Request (PR)
- Pull updates to your local machine
- Run tests and a style checker locally
- Submit a GitHub repository to Gradescope
- Read autograder output, fix issues, and resubmit
- Know how and where to attend instructor office hours

## Part 0 — Set up your tools

Before starting the repository workflow, make sure you have the required tools installed and working.

Use the setup guides below if you need to install or configure anything:

- [Python Setup Guide](https://amandakube.github.io/guides/python/installation-guide/)
- [VS Code Setup Guide](https://amandakube.github.io/guides/vscode/installation-guide/)
- [Git Setup Guide](https://amandakube.github.io/guides/git/installation-guide/)

If you already have a tool installed, you do **not** need to reinstall it. Follow the guide's verification steps to make sure your setup works.

If you run into a problem during installation, use the troubleshooting information in the relevant guide before continuing.

## Part 1 — GitHub and course repository setup

### Step 1A — Create a GitHub account

If you do not already have a GitHub account:

1. Go to [GitHub](https://github.com).
2. Create an account.
3. Choose a username you are comfortable using professionally.
4. Verify your email address.

If you already have a GitHub account, skip this step.

### Step 1B — Accept the course assignment via Classroom 50

1. Follow the instructions in your email.
2. Click the assignment link posted on Canvas.
2. Log in to GitHub if prompted.
3. Follow the instructions to create your course repository.
4. Wait for the repository to finish generating before continuing.

If you encounter an error or cannot access your repository, stop and ask for help before continuing.

## Part 2 — Clone your repository

### Step 2A — Open your repository on GitHub

After accepting the assignment, open the repository that was created for you.

You should see files including:

- `practice.py`
- `README.md`
- `requirements.txt`

### Step 2B — Copy the repository URL

1. Click the green **Code** button.
2. Make sure **HTTPS** is selected.
3. Copy the repository URL.

It will look similar to:

```text
https://github.com/<course-org>/<your-repository>.git
```

### Step 2C — Clone the repository

Open the terminal you use for this course and run:

```bash
git clone <PASTE_THE_URL_YOU_COPIED>
cd <your-repository>
```

**Cloning** creates a local copy of the repository on your computer.

You are now working **locally**.

If GitHub asks you to authenticate and you are unsure what to do, refer to the GitHub setup guide.

## Part 3 — Install the assignment requirements

This repository includes a `requirements.txt` file containing the Python packages needed for the assignment.

Run:

```bash
python -m pip install -r requirements.txt
```

This assignment uses:

- `pytest` — runs automated tests
- `pylint` — checks code style and identifies common problems

If installation fails, stop and ask for help before continuing.

## Part 4 — Work on a branch

### What is a branch?

A **branch** is a separate line of development.

- `main` contains the official version of your code.
- You will do your work on another branch and merge it into `main` when you are finished.

### Step 4A — Create a branch

Create a branch named `part-4`:

```bash
git checkout -b part-4
```

### Step 4B — Edit `practice.py`

Open `practice.py` in VS Code and complete the TODOs.

For this assignment, **only edit `practice.py`**.

Do not change:

- `.pylintrc`
- `.gitignore`
- `requirements.txt`

These files configure the tools used by the course workflow and autograder.

If you accidentally change one of them, restore them with:

```bash
git checkout -- .pylintrc .gitignore requirements.txt
```

## Part 5 — Test your work

### Step 5A — Run the tests

Run:

```bash
pytest
```

When `pytest` finishes, it will print a summary similar to:

```text
===================== 6 passed in 0.03s =====================
```

Copy the summary line and add it as a comment at the **top of `practice.py`**.

For example:

```python
# pytest output: ===================== 6 passed in 0.03s =====================
```

This is required.

The local tests are a small **smoke test**. Gradescope may run additional tests.

If your local tests pass but Gradescope reports a failure, read the Gradescope output carefully and update your code.

### Step 5B — Run the linter

Run:

```bash
pylint practice.py
```

A **linter** checks code style and common programming mistakes.

You do not need to understand every message yet. For this assignment, your goal is simply to successfully run the tool and begin getting familiar with its output.

Copy your Pylint score and add it below the `pytest` comment.

For example:

```python
# pytest output: ===================== 6 passed in 0.03s =====================
# pylint score: 4
```

This is required.

Do not worry about what is considered a "good" Pylint score yet.

## Part 6 — Commit and push your changes

**Committing** saves a snapshot of your work locally.

**Pushing** sends those commits to GitHub.

Run:

```bash
git add practice.py
git commit -m "Complete Assignment 0"
git push -u origin part-4
```

Then open your repository on GitHub and confirm that your branch and commit appear.

## Part 7 — Open and merge a Pull Request

A **Pull Request (PR)** is how you propose merging changes from one branch into another.

1. Open your repository on GitHub.
2. Click **Compare & pull request**.
3. Confirm that the PR shows:

```text
part-4 → main
```

4. Open the Pull Request.
5. Review your changes.
6. Click **Merge pull request**.

After merging, update your local copy:

```bash
git checkout main
git pull
```

Your completed work should now be on `main`.

## Part 8 — Submit to Gradescope

On Gradescope:

1. Open **Assignment 0**.
2. Choose **GitHub** as the submission method.
3. Select your repository.
4. Submit.

**Do not upload a ZIP file.**

If the autograder reports failures:

1. Fix the problem locally.
2. Run your tests again.
3. Commit the change.
4. Push it to GitHub.
5. Resubmit to Gradescope.

You may resubmit as needed.

## Part 9 — Come say hello at office hours

During the **first two weeks of the quarter**, attend **at least one office hour held by Professor Jotte or Professor Nussbaum** and introduce yourself.

You do **not** need to have a question or a problem to attend. You can simply stop by, introduce yourself, and say hello.

For this part of Assignment 0, **TA office hours do not count**. We specifically want each of you to meet one of your instructors early in the quarter.

The goal is to make sure you:

- know where and how to attend instructor office hours,
- meet at least one of your instructors,
- and feel comfortable coming back when you have questions or need help later in the quarter.

When you arrive, let Professor Jotte or Professor Nussbaum know that you are completing the **Assignment 0 introduction** so we can record that you stopped by.

## Completion verification

Assignment 0 is considered complete when all of the following are true:

- [ ] Python, VS Code, Git, and GitHub are set up
- [ ] Course repository created
- [ ] Repository cloned locally
- [ ] Branch created
- [ ] `practice.py` completed
- [ ] `pytest` run and output recorded in `practice.py`
- [ ] `pylint practice.py` run and score recorded
- [ ] Changes committed and pushed
- [ ] Pull Request opened and merged
- [ ] Local `main` updated with `git pull`
- [ ] Repository submitted to Gradescope
- [ ] Final Gradescope submission passes
- [ ] Attended Professor Jotte's or Professor Nussbaum's office hours during the first two weeks and introduced yourself

## Why this matters for the rest of the course

Future assignments will assume that you can:

- work with Git and GitHub,
- work with course repositories,
- run tests and linters locally,
- submit repositories to Gradescope,
- and interpret autograder feedback.

If you encounter technical issues later **and you did not complete this assignment**, those issues will **not** be grounds for deadline extensions or leniency.

## Getting help early

If something goes wrong:

- stop before making lots of additional changes,
- copy the **exact error message and command that caused it** as text so others can copy and paste it,
- check the relevant setup guide,
- and ask for help on Ed Discussion or during office hours.

This assignment is designed so that getting help now prevents bigger problems later.
