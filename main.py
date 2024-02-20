import argparse
import json

from kpu_client import KPUClient


def main(args):
    kpu_client = KPUClient()

    if args.task == 'collect-data':
        kpu_client.collect_data(args.target_file)

    if args.task == 'extract-image':
        if args.url != '':
            kpu_client.extract_image(url=args.url, target_path=args.target_path)
        else:
            kpu_client.extract_image(target_path=args.target_path)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task')
    parser.add_argument('--url')
    parser.add_argument('--target_file')
    parser.add_argument('--target_path')
    args = parser.parse_args()
    main(args)