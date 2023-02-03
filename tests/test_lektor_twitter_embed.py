import unittest.mock

import pytest
import requests

from lektor_twitter_embed import _init_params, _tweet


def _mock_request_valid(url, params):
    return {"html": "<blockquote..."}


def _mock_request_exception(url, params):
    raise requests.exceptions.HTTPError()


_tweet_url = "https://twitter.com/thisstuartlaws/status/1353838316198756352"


def test_init_params_none():
    assert _init_params(_tweet_url, None) == {
        "url": _tweet_url,
        "dnt": "true",
    }


def test_init_params_dict():
    assert _init_params(_tweet_url, {"dnt": "false", "align": "center"}) == {
        "url": _tweet_url,
        "dnt": "false",
        "align": "center",
    }


@unittest.mock.patch("lektor_twitter_embed._send_request", _mock_request_valid)
def test_tweet_valid():
    assert _tweet(_tweet_url) == "<blockquote..."


@unittest.mock.patch("lektor_twitter_embed._send_request", _mock_request_exception)
def test_tweet_exception_no_fallback():
    with pytest.raises(requests.exceptions.HTTPError):
        _tweet(_tweet_url)


@unittest.mock.patch("lektor_twitter_embed._send_request", _mock_request_exception)
def test_tweet_exception_with_fallback():
    assert (
        _tweet(_tweet_url, fallback=True) == f'<a href="{_tweet_url}">{_tweet_url}</a>'
    )
