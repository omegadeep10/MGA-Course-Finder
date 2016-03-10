from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    url = "http://mga.edu/course-schedule/index.php?quick=ALL&page=1&sort=subj&asc&term=201601"
    soup = BeautifulSoup(urlopen(url))
    print(soup.prettify)



if __name__ == '__main__':
    main()