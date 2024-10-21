import git
from git.exc import GitCommandError

def push_changes(repo_path, commit_message, branch='main'):
    """
    Push changes to a remote git repository.

    Args:
    repo_path (str): Path to the local git repository.
    commit_message (str): Commit message for the changes.
    branch (str): Branch to which the changes should be pushed. Defaults to 'main'.

    Returns:
    str: Success message or error message.
    """
    try:
        repo = git.Repo(repo_path)
        if not repo.is_dirty():
            return "No changes detected in the repository."
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push(refspec=f'{branch}:{branch}')
        return "Changes pushed successfully to the remote repository."
    except GitCommandError as e:
        return f"An error occurred while pushing changes: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"



push_changes()

