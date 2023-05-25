import tkinter as tk
from tkinter import filedialog
import os

def current_dir():
    # ルートウィンドウ作成
    root = tk.Tk()
    # ルートウィンドウの非表示
    root.withdraw()

    # 一つ前のディレクトリに移動
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    current_dir =os.getcwd()

    # ファイル選択
    target_dir = filedialog.askdirectory(initialdir = current_dir)

    # ルートウィンドウを削除
    root.destroy()

    return target_dir
