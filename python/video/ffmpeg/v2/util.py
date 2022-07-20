import os
import subprocess


def util_convert_video(source: str, output: str) -> int:
    try:
        folder = os.path.dirname(source)
        log_out = os.path.join(folder, "xcc.log")
        log_err = os.path.join(folder, "xcc-err.log")
        with open(log_out, "w") as stdout, open(log_err, "w") as stderr:
            cmd = ['ffmpeg', '-y', '-strict', '-2', '-i', source, output]
            return subprocess.call(cmd, stdout=stdout, stderr=stderr)
    except Exception as e:
        print(e)
    return -1


def util_split_name(filename: str, sep: str = ".") -> tuple[str, str]:
    if sep in filename:
        index = filename.rindex(sep)
        basename = filename[:index]
        extension = filename[index:]
        return basename, extension
    else:
        return filename, ''


def util_find_files(root: str, extensions: list[str] = [".mp4"]) -> list[str]:
    file_list: list[str] = []
    for root, dirs, files in os.walk(root):
        for filename in files:
            fullname = os.path.abspath(root + os.sep + filename)
            _, extension = util_split_name(filename)
            if extension in extensions:
                file_list.append(fullname)

    return file_list
