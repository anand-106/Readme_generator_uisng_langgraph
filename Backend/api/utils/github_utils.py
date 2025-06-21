import os
import shutil
from git import Repo
import tempfile
import requests

def clone_repo(url: str)->str:


    try:
        requests.get("https://github.com", timeout=5)
        print("Network access to GitHub is OK")
    except Exception as e:
        print(f"Network access to GitHub failed: {e}")

    tmp_dir = tempfile.mkdtemp(prefix="repo_")

    try:
        Repo.clone_from(url,tmp_dir)
        print(f"Repo cloned Sucessfully at {tmp_dir}")
        return tmp_dir
    except Exception as e:
        shutil.rmtree(tmp_dir,ignore_errors=False)
        raise Exception(f"Failed to clone repo: {e}")