# MDR XAFS Viewer

This is the very alpha version. Please try this at your own risk.

1. Download some data from MDR XAFS DB.

`mkdir data`

`cd util`

`python mdr_zip_dl_example.py https://mdr.nims.go.jp/catalog?q=Cu+BL14B2`

2.  Move \*.zip from util to data.
3.  Install required python modules.

`pip install -r requirements.txt`

4.  Run and pray it works.

`python main.py`
