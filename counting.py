from operator import itemgetter


def main():
    urls = input("Input a list of urls: ")
    urls = urls.strip('[]').split(',')
    count = {}

    for url in urls:
        filename = url.strip('"').split('/')[-1]
        if filename in count:
            count[filename] += 1
        else:
            count[filename] = 1

    sortedList = sorted(count.items(), key=itemgetter(1), reverse=True)
    for i in range(3):
        print(sortedList[i][0] + " " + str(sortedList[i][1]))


if __name__ == '__main__':
    main()
