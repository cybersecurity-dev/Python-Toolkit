import os

def is_elf_file(fpath) -> bool:
    """
    Checks if a file looks like an ELF by its magic bytes.
    """
    try:
        with open(fpath, 'rb') as f:
            magic = f.read(4)
            return magic == b'\x7fELF'
    except OSError:
        return False

def file_has_execute_permissions(fpath: str) -> bool:
    """
    Checks if the current user can execute the file.
    """
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
