from pathlib import Path

if __name__ == "__main__":
    data_dir = "04/exercise/data" #dir右クリックで相対パスを取得からとれる
    data_dir = Path(data_dir).resolve()
    print("===== problem1 =====")
    print("===== absolute path =====")
    print(data_dir)

    print("===== problem2 =====")
    print("===== all under the data_dir =====")
    file_list = list(data_dir.glob("*"))
    for path in enumerate(file_list):
        print(path[1])

    print("===== problem3 =====")
    file2_list = list(data_dir.glob("**/*.png"))
    print(len(file2_list))
    