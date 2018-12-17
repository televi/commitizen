import pytest
from commitizen.cz.conventional_commits.conventional_commits import (
    parse_scope,
    parse_subject,
    NoSubjectException,
)


valid_scopes = ["", "simple", "dash-separated", "camelCase" "UPPERCASE"]

scopes_transformations = [["with spaces", "with-spaces"], [None, ""]]

valid_subjects = ["this is a normal text", "aword"]

subjects_transformations = [["with dot.", "with dot"]]

invalid_subjects = ["", "   ", ".", "   .", "", None]


def test_parse_scope_valid_values():
    for valid_scope in valid_scopes:
        assert valid_scope == parse_scope(valid_scope)


def test_scopes_transformations():
    for scopes_transformation in scopes_transformations:
        invalid_scope, transformed_scope = scopes_transformation
        assert transformed_scope == parse_scope(invalid_scope)


def test_parse_subject_valid_values():
    for valid_subject in valid_subjects:
        assert valid_subject == parse_subject(valid_subject)


def test_parse_subject_invalid_values():
    for valid_subject in invalid_subjects:
        with pytest.raises(NoSubjectException):
            parse_subject(valid_subject)


def test_subject_transformations():
    for subject_transformation in subjects_transformations:
        invalid_subject, transformed_subject = subject_transformation
        assert transformed_subject == parse_subject(invalid_subject)
