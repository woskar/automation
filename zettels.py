'''
A python script to get exercise sheets downloaded from the web
'''

#import webbrowser
#webbrowser.open('http://inventwithpython.com/')

import requests, os, bs4

url = 'https://uebungen.physik.uni-heidelberg.de/vorlesung/20172/pep5' # starting url
location = '/Users/Oskar/Dropbox/PEP5'

#os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")

# Find the URL of the pdf files
zettels = soup.select('#infoarea-3922 a')
if zettels == []:
    print('Could not find Übungsblätter in id=infoarea-3922')
else:
    print('Selected elements from webpage:')
    print(zettels)

    for zettel in zettels:
        name = zettel.getText()
        if os.path.isfile(location + '/' + name):
            print('File', name, 'already exisits at', location, '.')
            continue
        else:
            print('New File found, now saving...')

            zettelURL = 'https://uebungen.physik.uni-heidelberg.de' + zettel.get('href')
            print(zettelURL)
            res = requests.get(zettelURL)
            res.raise_for_status()

            zettelFile = open(os.path.join(location, name), 'wb')
            for chunk in res.iter_content(100000):
                zettelFile.write(chunk)
            zettelFile.close()

print('Done')



'''
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
'''




 