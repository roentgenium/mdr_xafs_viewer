.. warning::
    This is the very alpha version. Please try this at your own risk.

1. Download some data from MDR XAFS DB.

:code:`python util/mdr_zip_dl_example.py`

or

:code:`python util/mdr_zip_dl_example.py "https://mdr.nims.go.jp/catalog?utf8=%E2%9C%93&f%5Bmember_of_collections_ssim%5D%5B%5D=MDR+XAFS+DB&locale=en&search_field=all_fields&q=Fe+transmission"`

2. Copy \*.zip from util to data.
3. Install required python modules.

:code:`pip install -r requirements.txt`

4. Run and pray it works.

:code:`python main.py`
