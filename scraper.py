from string import Template

from bs4 import BeautifulSoup
from requests import get

"""
All video embed urls follow the template `https://www.ndtv.com/video/embed-player/?id=ID`
Further parameters like height and width of display, autostart and autoplay can also be added to the embed url
Currently using only the necessary options
"""
embed_url = Template('https://www.ndtv.com/video/embed-player/?id=$id')


def fetch_video_embed_links(url: str):
    """
    Function to get all video embed links from a given URL
    :param url: URL of page from which we have to fetch video embed links
    :return: Set of all video embed links
    """
    html = get(url).text
    soup = BeautifulSoup(html, features="html.parser")

    links = set()  # set of all video embed links

    return links


if __name__ == "__main__":
    links = fetch_video_embed_links('https://www.ndtv.com/video')
    print(*links, sep="\n")
