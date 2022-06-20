from modules.helpers import *
from modules.sqlite import *
import os
import random


def midnight():
    targetList = inputList()
    titlePrinter()
    rootcheck()
    masterList = []
    while len(targetList) > 0:
        if not os.path.exists("../output/midnight.db"):
            createDB()
        midnightCon = connectDB()
        createTables(midnightCon)
        url = random.choice(targetList)
        torstatus()
        extensions = ('.jpg', 'jpeg', '.mp4', '.png', '.gif')
        # This is for any site that makes the program hang excessively long
        blacklist = ('http://76qugh5bey5gum7l.onion')
        if url not in masterList and not url.endswith(extensions) and not url.startswith(blacklist):
            print("New iteration:")
            print("Currently scanning " + url)
            status = onionStatus(url)
            if status != 404:
                html = onionHTML(url)
                if html == "None":
                    targetList.remove(url)
                    print("Returned TraceError. Moving to next URL")
                else:
                    res = []
                    onions = onionExtractor(html, url)
                    atag = aTag(url, html)
                    allonions = onions + atag
                    onionResults = list(set(allonions))
                    for site in onionResults:
                        if site not in res:
                            res.append(site)
                    newList = inputAdder(onions, targetList)
                    masterList.append(url)
                    if url in newList:
                        newList.remove(url)
                    targetList = newList
                    print("Number of sites found: " + str(len(res)))
                    url, urlDir = urlSplitter(url)
                    if urlDir == "":
                        urlDir = "/"
                    data = addDeepData(url, urlDir, html, midnightCon)
                    for connection in res:
                        site, siteDir = urlSplitter(connection)
                        if siteDir == "":
                            siteDir = "/"
                        connections = addDeepConnections(
                            url, urlDir, site, siteDir, midnightCon)
            else:
                targetList.remove(url)
                print("URL gave bad response...not scanning")
        elif url in masterList:
            targetList.remove(url)
            print(url)
            print("URL already scanned")
        elif url.startswith(blacklist):
            targetList.remove(url)
            print(url)
            print("URL in blacklist")
        elif url.endswith(extensions):
            targetList.remove(url)
            print(url)
            print("URL ends with extension not compatible")
    '''
    #Keeps the program running indefinitely
        while True:
            python = sys.executable
            os.execl(python, python, *sys.argv)
    '''


if __name__ == '__main__':
    midnight()
