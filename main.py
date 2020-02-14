# ----------------------------
# 094
# 書き込んだ後、読み込む → ファイルの保存形式があっているか。。
# 読み込んだ後、書き込む → 追記。。
# https://docs.python.org/ja/3/tutorial/inputoutput.html#reading-and-writing-files
# 注意、seekで場所を移動してから次の読み書きをすること
# ----------------------------

# 書き込んだ後、読み込む
# "w"で開かれた時点で空ファイルが上書きされる
# 実用ではファイルが存在している場合、確認するなどの機能が必要かも
filename = r"./test.txt"
with open(filename, "w+") as f:
    f.write("AAA\nBBB\n")

    # 書き込んだ後は最終行にいる
    currentLocation = f.tell()
    print(currentLocation)

    # 読み込み開始位置を先頭にする
    f.seek(0)
    print(f.read())

# 読み込んだ後、書き込む
# 該当ファイルがない場合→FileNotFoundError
with open(filename, "r+") as f:
    fileData = f.read()
    # 読み込んだ後は最終行にいる
    currentLocation = f.tell()
    print(currentLocation)

    # 最終行に追加
    f.write("CCC\nDDD\n")
