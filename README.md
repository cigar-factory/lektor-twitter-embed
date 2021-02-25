# lektor-twitter-embed

[![Run tests](https://github.com/cigar-factory/lektor-twitter-embed/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/cigar-factory/lektor-twitter-embed/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cigar-factory/lektor-twitter-embed/branch/main/graph/badge.svg?token=teWLUZntKT)](https://codecov.io/gh/cigar-factory/lektor-twitter-embed)
[![PyPI Version](https://img.shields.io/pypi/v/lektor-twitter-embed.svg)](https://pypi.org/project/lektor-twitter-embed/)
![License](https://img.shields.io/pypi/l/lektor-twitter-embed.svg)
![Python Compatibility](https://img.shields.io/badge/dynamic/json?query=info.requires_python&label=python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Flektor-twitter-embed%2Fjson)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

Lektor template filter to convert twitter links to embeds

## Installation

```
pip install lektor-twitter-embed
```

## Usage

```
{{ "https://twitter.com/MaiaFranklyn/status/1277100235928621058" | tweet }}
```

It is possible to pass an optional 'params' object to configure the embed.
Any of the params documented at
https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-oembed
may be supplied

```
{{
  "https://twitter.com/MaiaFranklyn/status/1277100235928621058" | tweet(
    params={'align': 'center', 'hide_thread': 'true'}
  )
}}
```

By default if the request to `publish.twitter.com` fails, your page will not build.
This behaviour can be changed so that a failed request to `publish.twitter.com` will fall back to rendering a link to the tweet.

```
{{ "https://twitter.com/lucaviftw/status/1347311486012686336" | tweet(fallback=True) }}
```
