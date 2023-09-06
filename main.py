import requests

def get_artists(date1):
    """

    :param date:
    :return:
    """
    url = "https://www.comedycellar.com/lineup/api/"

    payload = 'action=cc_get_shows&json={"date":"2023-09-06","venue":"newyork","type":"lineup"}'
    headers = {
        'Host': 'www.comedycellar.com',
        'Content-Length': '80',
        'Sec-Ch-Ua': '',
        'Sec-Ch-Ua-Platform': '""',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'https://www.comedycellar.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.comedycellar.com/new-york-line-up/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'AWSALB=J9iRjMZC2ozb1g5jKa5kxQ0/oiZX8ayED53Meaws/lV0E5NnmPMP7Jyj//5eydoMkrNU4yS/y8OjnSQoBmVy/S3e+joNKEzVEo0dKZ80q4cfqP/ckMve4ni1hjmg; AWSALBCORS=J9iRjMZC2ozb1g5jKa5kxQ0/oiZX8ayED53Meaws/lV0E5NnmPMP7Jyj//5eydoMkrNU4yS/y8OjnSQoBmVy/S3e+joNKEzVEo0dKZ80q4cfqP/ckMve4ni1hjmg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

def find_artist(artistName, allArtists):
    """

    :param allArtists: list of all artists
    :param artistName: name of the artist you want to find
    :return: True if artist name is found
    """

    if artistName.lower() in allArtists.lower():
        return True
    else:
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    all_shows = (get_artists("2023-09-06"))
    print(find_artist("aNdrew", all_shows))

