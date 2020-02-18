"""Test to ensure that the functions in the cookbook-style program are correct."""

from find_tests import commits_to_testing

def test_read_file_populates_data_0():
    """Checks that the size of the input variable is correct."""
    commit_author_list = []
    assert len(commits_to_testing.commit_author_list) == 0
    commits_to_testing.find_testing_commits()
    assert len(commits_to_testing.commit_author_list) != 0
