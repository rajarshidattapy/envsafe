import pytest
from envsafe import env
from envsafe.exceptions import EnvError


def test_str(monkeypatch):
    monkeypatch.setenv("A", "hello")
    assert env.str("A") == "hello"


def test_missing():
    with pytest.raises(EnvError):
        env.str("MISSING")


def test_int(monkeypatch):
    monkeypatch.setenv("N", "10")
    assert env.int("N") == 10


def test_bool(monkeypatch):
    monkeypatch.setenv("B", "true")
    assert env.bool("B") is True


def test_list(monkeypatch):
    monkeypatch.setenv("L", "a,b,c")
    assert env.list("L") == ["a", "b", "c"]


def test_json(monkeypatch):
    monkeypatch.setenv("J", '{"a":1}')
    assert env.json("J") == {"a": 1}
