from github import Github
from config import GITHUB_REPO, GITHUB_TOKEN

def get_open_prs():
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(GITHUB_REPO)
    return repo.get_pulls(state="open")

def get_pr_files(pr):
    return [file for file in pr.get_files()]

if __name__ == "__main__":
    prs = get_open_prs()
    for pr in prs:
        print(f"PR #{pr.number}: {pr.title}")
        for file in get_pr_files(pr):
            print(f"File: {file.filename}\nDiff:\n{file.patch}\n")
