# #!/home/kenno/.pyenv/shims/python3
# tpyecode.py
"""型判定モジュール."""


def judgement(
    code: str | int | float | bytes | object | list | tuple | dict | set,
) -> type:
    """型を判定する関数."""
    return type(code)


# if __name__ == '__main__':