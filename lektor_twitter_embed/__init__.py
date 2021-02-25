import requests
from jinja2 import Markup
from lektor.pluginsystem import Plugin


def _init_params(url, params):
    if not params:
        params = {}
    params["url"] = url
    if "dnt" not in params:
        params["dnt"] = "true"
    return params


def _send_request(url, params):
    r = requests.get("https://publish.twitter.com/oembed", params=params)
    r.raise_for_status()
    return r.json()


def _tweet(url, params=None, fallback=False):
    try:
        json_ = _send_request(
            "https://publish.twitter.com/oembed", _init_params(url, params)
        )
    except requests.exceptions.RequestException:
        if fallback:
            return Markup('<a href="{url}">{url}</a>'.format(url=url))
        raise

    return Markup(json_["html"])


class TwitterEmbedPlugin(Plugin):
    name = "lektor-twitter-embed"

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters["tweet"] = _tweet
