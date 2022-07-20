import os
import time

from util import util_find_files, util_split_name, util_convert_video


def main():
    root = "E:\\codec"
    output_format = ".webm"
    if not os.path.exists(root):
        return
    filename_list = util_find_files(root, [".mp4"])
    for file_path in filename_list:
        fullname = os.path.abspath(file_path)
        input_name = os.path.basename(fullname)
        folder = os.path.dirname(fullname)
        file_name, _ = util_split_name(input_name)
        output_name = file_name + output_format
        output = os.path.join(folder, output_name)
        print("%s ==> %s" % (input_name, output_name))
        begin = time.time()
        # time.sleep(15 * random.random() + 5.0)
        util_convert_video(fullname, output)
        end = time.time()
        offset = int(end - begin)
        print("xcc spends %ds for %s" % (offset, input_name))


if __name__ == '__main__':
    main()
