import os
import json
import requests

LEETCODE_API_URL = 'https://leetcode.com/api/problems'
SHIELDS_IO_BADGE_URL = 'https://img.shields.io/badge'
DIFFICULTY_LUT = {
    1: {
        'name': 'Easy',
        'color': 'green',
    },
    2: {
        'name': 'Medium',
        'color': 'yellow',
    },
    3: {
        'name': 'Hard',
        'color': 'red',
    },
}
CATEGORIES_FILE = 'categories.json'

def leetcode_api(category):
    url = f'{LEETCODE_API_URL}/{category.lower()}/'

    response = requests.get(url)
    response_json = response.json()

    data = {}
    stat_status_pairs = response_json.get('stat_status_pairs')
    for question in stat_status_pairs:
        question_id = question.get('stat').get('frontend_question_id')
        question_title = question.get('stat').get('question__title')
        difficulty = DIFFICULTY_LUT.get(question.get('difficulty').get('level'))

        data[question_id] = {
            'title': question_title,
            'difficulty': difficulty,
        }

    return data

def categories_data():
    with open(CATEGORIES_FILE) as categories_file:
        categories = json.load(categories_file)

    return categories

def difficulty_shields_io(difficulty):
    name = difficulty.get('name')
    color = difficulty.get('color')
    shield = f'{SHIELDS_IO_BADGE_URL}/{name}-{color}'

    return shield

if __name__ == '__main__':
    with open('../README.md', 'w') as readme_file:
        readme_file.write('# LeetCode Problems & Solutions\n\n')
        readme_file.write('<img alt="LeetCode Logo" src="img/leetcode_logo.png" width="400"/>\n\n')
        readme_file.write('This repository contains solutions to [LeetCode](https://leetcode.com/) problems.\n\n')

        categories = categories_data()
        for category in categories:
            name = category.get('name')
            logo = category.get('logo')
            data = leetcode_api(name)

            readme_file.write(f'## {name}\n\n')
            readme_file.write(f'<img alt="{name} Logo" src={logo} width="100"/>\n\n')
            readme_file.write('No. | Problem | Difficulty\n')
            readme_file.write('--- | --- | ---\n')

            for problem_dir in os.listdir(f'../{name}/'):
                problem_id = problem_dir.split('_')[0]

                problem_data = data.get(int(problem_id))
                title = problem_data.get('title')

                difficulty = problem_data.get('difficulty')
                difficulty_shield = difficulty_shields_io(difficulty)

                readme_file.write(f'{problem_id} | [{title}]({name}/{problem_dir}) | ![Difficulty]({difficulty_shield})\n')

            readme_file.write('\n')