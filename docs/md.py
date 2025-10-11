import argparse
import requests
from markdownify import markdownify as md

PROGRAM_NAME = 'leetcode-md'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    parser.add_argument('--html', action='store_true')

    args = parser.parse_args()

    response = requests.get(f'https://leetcode-api-pied.vercel.app/problem/{args.id}')
    response.raise_for_status()
    data = response.json()

    if args.html:
        content = f'<h1>{data['title']}</h1>\n\n{data['content']}'
    else:
        content = f'# {data['title']}\n\n{md(data['content'])}'

    print(content)
