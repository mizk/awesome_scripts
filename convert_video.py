import os


def convert(source, output):
    cmd = 'ffmpeg -i "{0}" -c copy "{1}"'.format(source, output)
    c = os.system(cmd)
    return c


def main():
    storage = "/Users/xxx/Movies/yyy"
    for root, dirs, files in os.walk(storage):
        for file in files:
            fi = root + "/" + file
            fi = fi.lower()
            if fi.endswith(".mkv"):
                output = fi.replace(".mkv", ".mp4")
                print("convert {0} to {1}".format(fi, output))
                convert(fi, output)


if __name__ == '__main__':
    main()
