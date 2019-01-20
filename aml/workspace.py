import argparse
from azureml.core.workspace import Workspace

def main(args):
    ws = Workspace.get(subscription_id=args.id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ws')
    parser.add_argument('--id')
    parser.add_argument('--group')
    args = parser.parse_args()
    print(args)
