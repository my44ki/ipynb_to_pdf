import tkinter as tk
import os
import glob
from PyPDF2 import PdfMerger, PdfFileReader
import nbformat
from nbconvert import PDFExporter
from get_current_folder import current_dir

# Tkinterのテストウィンドウを表示
tk._test()

# 現在のフォルダパスを取得
folder_path = os.path.normpath(current_dir())

# pdf フォルダーを作成
os.makedirs(os.path.join(folder_path, 'pdf'), exist_ok=True)
pdf_folder = os.path.join(folder_path, 'pdf')

def convert_ipynb_to_pdf(ipynb_file, pdf_file):
    # 変換させたいipynbファイルのカレントディレクトリに移動
    os.chdir(os.path.dirname(ipynb_file))
    
    # .ipynbファイルを読み込む
    with open(ipynb_file, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)
        
    # タイトルを設定
    ipynb_name = os.path.basename(ipynb_file).replace('.ipynb','')
    nb.metadata["title"] = f'{ipynb_name}'

    # PDFエクスポーターを作成
    pdf_exporter = PDFExporter()
    pdf_exporter.exclude_input_prompt = True
    pdf_exporter.exclude_output_prompt = True

    # .ipynbをPDFに変換して保存
    (body, resources) = pdf_exporter.from_notebook_node(nb)
    with open(pdf_file, "wb") as f:
        f.write(body)

# dir_path にあるフォルダー内の pdf を抽出し、dst_path という path も込みのフォルダー名で出力
def merge_pdf_in_dir(dir_path, dst_path):
    pdf_files = glob.glob(os.path.join(dir_path, '*.pdf'))
    pdf_files.sort()

    merger = PdfMerger()
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as f:
            if not PdfFileReader(f).isEncrypted:
                merger.append(f)

    with open(dst_path, 'wb') as f:
        merger.write(f)

    merger.close()

def run_merge_pdf(folder_path):
    # pdf フォルダーを作成
    os.makedirs(os.path.join(folder_path, 'pdf'), exist_ok=True)
    pdf_folder = os.path.join(folder_path, 'pdf')
    
    # pdf ファイルへ変換
    for ipynb_file in sorted(glob.glob(os.path.join(folder_path, '*.ipynb'))):
        pdf_file = os.path.basename(ipynb_file).replace('.ipynb', '.pdf')
        convert_ipynb_to_pdf(ipynb_file, os.path.join(pdf_folder,pdf_file))
    
    # マージさせる
    merge_pdf_in_dir(os.path.join(folder_path,'pdf'), os.path.join(folder_path, f'{os.path.basename(folder_path)}.pdf'))

run_merge_pdf(folder_path)