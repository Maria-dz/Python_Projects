import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser(description='Ping script')
parser.add_argument('--key', default=None, dest='key')
parser.add_argument('--val', default=None, dest='val')
args = parser.parse_args()

if not args.key:
    print(None)
else:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if not os.path.exists(storage_path) and not args.val:
        print(None)
    elif not args.val:
        with open(storage_path, 'r') as f:
            inside = json.loads(f.read())
        if args.key not in inside:
            print(None)
        else:
            print(', '.join(inside[args.key]))
    elif not os.path.exists(storage_path):
        dict = {}
        dict[args.key] = [args.val]
        with open(storage_path, 'w') as f:
            f.write(json.dumps(dict))
    else:
        with open(storage_path, 'r') as f:
            inside = json.loads(f.read())
            if args.key not in inside:
                inside[args.key] = []
            inside[args.key].append(args.val)
            with open(storage_path, 'w') as f:
                f.write(json.dumps(inside))





