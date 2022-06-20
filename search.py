from modules.sqlite import *
from modules.helpers import *


def main():
    try:
        searchTitle()
        con = connectDB()
        createFTStable(con)
        populateFTS(con)
        searchTitle()
        try:
            while(True):
                term = input("Enter search term: ")
                results = searchFTS(term, con)
                print("Found " + str(len(results)) + " results.")

                for i in results:
                    string = ""
                    for j in i:
                        string += j
                    print(string)
        except KeyboardInterrupt:
            print('\n\nBye...')
    except:
        print("It looks like you didn't runned midnight yet.\nThere's no db for us to search. \nYou must run: python3 midnight.py \nbefore you can search")


if __name__ == '__main__':
    main()
