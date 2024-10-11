import os


def list_files(directory):
    # 遍历目录下的所有文件和文件夹
    for root, dirs, files in os.walk(directory):
        for index, file in enumerate(files):
            # 打印文件的完整路径
            text = fr"https://raw.githubusercontent.com/yangyanzhao/dayu_widgets/refs/heads/master/screenshots/{file}"
            t = fr"![screenshots/alert_dark.png]({text})"
            print(t)
            index += 1
            if index % 2 == 0:
                print("*" * 6)


# 示例目录
directory = r'D:\pythonwork\dayu_widgets\screenshots'
list_files(directory)
