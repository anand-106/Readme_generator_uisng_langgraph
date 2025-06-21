import os
import shutil
from git import Repo
import tempfile

def clone_repo(url: str)->str:

    tmp_dir = tempfile.mkdtemp(prefix="repo_")

    try:
        Repo.clone_from(url,tmp_dir)
        print(f"Repo cloned Sucessfully at {tmp_dir}")
        return tmp_dir
    except Exception as e:
        shutil.rmtree(tmp_dir,ignore_errors=False)
        raise Exception(f"Failed to clone repo: {e}")