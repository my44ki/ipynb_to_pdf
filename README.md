# ipynb_to_pdf
複数ある ipynb を pdf へ変換して結合する手間をなくすものです。

## Abstract

フォルダー内にある複数の ipynb ファイルを同ディレクトリ内に pdf フォルダーを作り、各 ipynb ファイルを変換して、 pdf ファイルにしたものを pdf フォルダーに収納する。最後に収納した pdf データを結合して、ipynb ファイルがあるディレクトリ直下に作成する。

## Prerequisites

conda == 23.3.1  
python == 3.8.16  
jupyter lab == 3.5.3  
tkinter == 8.6.12  
glob == 0.7  
pyPDF2 == 2.10.5  
nbformat == 5.7.0  
nbconvert == 6.5.4  

## Installing

    git clone https://github.com/my44ki/ipynb_to_pdf

## Usage
jupyter 上で `ipynb_to_pdf.py` を実行してもらう。  

例
```
%run ipynb_to_pdf.py
```
実行をすると tkinter の小ウィンドウが開くので適当な操作で複数の ipynb ファイルを変換したいファイルが保存されているディレクトリを指定する。  



## Authors
mail to: sirasakisouji@gmail.com

## License
  
[MIT](http://TomoakiTANAKA.mit-license.org)</blockquote>
