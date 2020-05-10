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

    """
    All urls to articles follow the format 
    `https://www.ndtv.com/video/special/article-title-ID?video-category`
    Hence, to fetch all ids (required to generate embed url), we simply need to extract the ID from the url.
    """

    # fetch all video descriptions (url to article is in anchor tag inside video description div)
    video_descriptions = soup.find_all('div', {'class': "video_description"})
    for vid_desc in video_descriptions:
        href = vid_desc.find('a').get('href')  # fetch article url from anchor tag
        video_id = href.split('?')[0].split('-')[-1]  # extract id from url

        # add generated embed url to set
        links.add(embed_url.substitute({'id': video_id}))

    return links


if __name__ == "__main__":
    links = fetch_video_embed_links('https://www.ndtv.com/video')
    print(*links, sep="\n")
