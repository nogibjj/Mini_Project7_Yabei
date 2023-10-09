"""
Test goes here
"""

import subprocess

def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout

def test_transform_load():
    """tests transform_load()"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming and loading data..." in result.stdout

def test_general_query():
    """tests general_query()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            """SELECT Performer, Show, Show_Start,Show_End
            FROM showdataDB
            GROUP BY Performer, Show
            ORDER BY Show_Start DESC
            LIMIT 10""",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0

if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()
