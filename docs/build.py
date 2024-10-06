import os
import json
import requests

LEETCODE_API_URL = 'https://leetcode.com/api/problems'
SHIELDS_IO_BADGE_URL = 'https://img.shields.io/badge'
DIFFICULTY_LUT = {
    1: {
        'name': 'Easy',
        'color': 'lawngreen',
    },
    2: {
        'name': 'Medium',
        'color': 'gold',
    },
    3: {
        'name': 'Hard',
        'color': 'orangered',
    },
}
CATEGORY_LOGOS = {
    'Algorithms': 'docs/img/algorithms_logo.png',
    'Database': 'docs/img/database_logo.png',
    'Shell': 'docs/img/shell_logo.png',
    'Concurrency': 'docs/img/concurrency_logo.png',
}
LANGUAGE_LOGOS = {
    'Bash': 'bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=000000',
    'Go': 'go-00ADD8?style=for-the-badge&logo=go&logoColor=FFFFFF',
    'MySQL': 'mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=F29111',
    'Python': 'python-3670A0?style=for-the-badge&logo=python&logoColor=FFDD54',
}

def leetcode_api(category):
    url = f'{LEETCODE_API_URL}/{category.lower()}/'

    response = requests.get(url)
    response_json = response.json()

    data = {}
    free_count = 0
    stat_status_pairs = response_json.get('stat_status_pairs')
    for question in stat_status_pairs:
        question_id = question.get('stat').get('frontend_question_id')
        question_title = question.get('stat').get('question__title')
        difficulty = DIFFICULTY_LUT.get(question.get('difficulty').get('level'))
        if question.get('paid_only') == False:
            free_count += 1

        data[question_id] = {
            'title': question_title,
            'difficulty': difficulty,
        }

    return data, free_count

def difficulty_shields_io(difficulty):
    name = difficulty.get('name')
    color = difficulty.get('color')
    shield = f'{SHIELDS_IO_BADGE_URL}/{name}-{color}'

    return shield

if __name__ == '__main__':
    with open('../README.md', 'w') as readme_file:
        readme_file.write('# LeetCode Problems & Solutions\n\n')
        readme_file.write('<img alt="LeetCode Logo" src="docs/img/leetcode_logo.png" width="400"/>\n\n')
        readme_file.write('This repository contains solutions to [LeetCode](https://leetcode.com/) problems.\n\n')

        for category_name, category_logo in CATEGORY_LOGOS.items():
            data, free_count = leetcode_api(category_name)

            listdir = os.listdir(f'../{category_name}/')
            listdir = sorted(listdir, key=lambda x: int(x.split('_')[0]))

            progress_bar = 'https://progress-bar.xyz/' + str(round((len(listdir) / free_count) * 100))

            readme_file.write(f'## {category_name}\n\n')
            readme_file.write(f'<img alt="{category_name} Logo" src={category_logo} width="100"/>\n\n')
            readme_file.write(f'Completed **{len(listdir)}** out of **{free_count}** (unpaid) problems\n\n')
            readme_file.write(f'![Progress Bar]({progress_bar})\n\n')
            readme_file.write('No. | Problem | Difficulty | Languages\n')
            readme_file.write('--- | --- | --- | ---\n')

            for problem_dir in listdir:
                problem_id = problem_dir.split('_')[0]

                problem_data = data.get(int(problem_id))
                title = problem_data.get('title')

                difficulty = problem_data.get('difficulty')
                difficulty_shield = difficulty_shields_io(difficulty)

                language_badges = ' '.join([f'![]({SHIELDS_IO_BADGE_URL}/{LANGUAGE_LOGOS[language]})' for language in os.listdir(f'../{category_name}/{problem_dir}') if language in LANGUAGE_LOGOS])

                readme_file.write(f'{problem_id} | [{title}]({category_name}/{problem_dir}) | ![Difficulty]({difficulty_shield}) | {language_badges}\n')

            readme_file.write('\n')
