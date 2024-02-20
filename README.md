# Indonesian Presidential Election 2024 Data

This repository consist of Indonesian Presidential Election 2024 dataset. The dataset consists of the final vote results per polling station.

## Files

The dataset can be obtained [here](https://drive.google.com/drive/folders/1rf9uyAhKSJSwMmq4nWY4M3xI0rdDWEAP?usp=sharing)

### Voting Results File
The voting results can be found under `raw_district_counts_<date>.json`, where `date` is the date the dataset was extracted.
The dataset consist of multiple lines of json. Each json follows this structure
```
{
	"url": URL_TO_KPU_API, 
	"data": {
		"chart": {
			"null": null,
			"100025": VOTE_COUNT_PASLON_1,
			"100026": VOTE_COUNT_PASLON_2,
			"100027": VOTE_COUNT_PASLON_3
		}, 
		"images": [C1_FORM_1_LINK, C1_FORM_2_LINK, C1_FORM_3_LINK], 
		"administrasi": {
			"suara_sah": 136,
			"suara_total": 142,
			"pemilih_dpt_j": 156,
			"pemilih_dpt_l": 74,
			"pemilih_dpt_p": 82,
			"pengguna_dpt_j": 140,
			"pengguna_dpt_l": 65,
			"pengguna_dpt_p": 75,
			"pengguna_dptb_j": 0,
			"pengguna_dptb_l": 0,
			"pengguna_dptb_p": 0,
			"suara_tidak_sah": 6,
			"pengguna_total_j": 142,
			"pengguna_total_l": 66,
			"pengguna_total_p": 76,
			"pengguna_non_dpt_j": 2, 
			"pengguna_non_dpt_l": 1, 
			"pengguna_non_dpt_p": 1
		}, 
		"psu": null, 
		"ts": "2024-02-16 09:30:28", 
		"status_suara": true, 
		"status_adm": true
	}
}
```
Some of the value might be None or null, which indicates that the voting results for the particular polling station yet to be uploaded.

The API also provides images link to the C1 form under `images` key.

### URLs
We also provides list of all urls API to obtain the above KPU dataset under `urls.json`

## Installation
create virtualenv
```
python -m venv env
source env/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```

## Download files
You can download the above files by following the link, or using gdown.
You just need to find the file id from drive and run the following command:
```
 gdown https://drive.google.com/uc\?id\=<FILE_ID>
```
E.g., for `district_counts_18_2_2024.json` , link to gdrive is : https://drive.google.com/file/d/<b>11gsCs8npDV_2Eanaw94rGGna9wzXTV8A</b>/view?usp=drive_link
```
 gdown https://drive.google.com/uc\?id\=11gsCs8npDV_2Eanaw94rGGna9wzXTV8A
```
For `urls.json`, run the following command (this command is neccessary to run data extractor below):
```
https://drive.google.com/file/d/1cUWd0OyBprz6TNJHxceyEBLRCstzU1VY/view?usp=drive_link
```
## Obtain the dataset
Run this command to call the API and obtain the dataset:
```
python main.py --task collect-data --target_file <TARGET_FILE>
```


## Obtain C1-form scanned image

Run this command to download the scanned C1-form:
```
python main.py --task extract-image  --url <URL> --target_path <TARGET_PATH> 
```
It will download C1-form images for a particular URL (Polling station) to the target path.

Run this command to download scanned C1-form for all polling station

```
python main.py --task extract-image  --url <URL> --target_path <TARGET_PATH> 
```
