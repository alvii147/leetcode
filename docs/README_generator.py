import os
import json

with open('categories.json') as categories_file:
    categories = json.load(categories_file)

with open('../README.md', 'w') as readme_file:
    readme_file.write('# LeetCode Problems\n\n')
    readme_file.write('<img alt="LeetCode Logo" src="img/leetcode_logo.png" width="400"/>\n\n')
    readme_file.write('This repository contains solutions to [LeetCode](https://leetcode.com/) problems.\n\n')
    for category in categories:
        name = category.get('name')
        logo = category.get('logo')

        readme_file.write(f'## {name}\n\n')
        readme_file.write(f'<img alt="{name} Logo" src={logo} width="100"/>\n\n')

        for problem_dir in os.listdir(f'../{name}/'):
            problem_name = ' '.join(problem_dir.split('_')[1:])
            readme_file.write(f'- [x] [{problem_name}]({name}/{problem_dir})\n')

        readme_file.write('\n')