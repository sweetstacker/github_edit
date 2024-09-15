import requests
import datetime
import os
import subprocess

# Setting
GITHUB_TOKEN = 'user-token'
REPO_NAME = 'repo-name'
START_DATE = datetime.date(2099, 1, 1) #날짜넣기 
END_DATE = datetime.date.today()
GITHUB_USERNAME = 'username'
REPEAT = 1000

# 레포생성함수
def create_github_repo():
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    data = {
        'name': REPO_NAME,
        'private': False #true로 할 경우 프라이빗해짐~
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print('Repository created successfully')
    else:
        print('Failed to create repository')
        print(response.json())

# 에브리데이커밋생성함수
def create_commits():
    current_date = START_DATE
    while current_date <= END_DATE:
        # 로컬파일생성
        repo_path = os.path.join(os.getcwd(), REPO_NAME)
        os.makedirs(repo_path, exist_ok=True)
        file_path = os.path.join(repo_path, f'file_{current_date}.txt')

        for commit_num in range(REPEAT):  #REPEAT번반복기계
            file_path = os.path.join(repo_path, f'file_{current_date}_part{commit_num}.txt')

            # 기록조작
            with open(file_path, 'w') as f:
                f.write(f'Commit for {current_date} - Part {commit_num}\n')

            # Git레포초기화
            subprocess.run(['git', 'init'], cwd=repo_path, check=True)
            
            # Git유저세팅
            subprocess.run(['git', 'config', 'user.name', 'username'], cwd=repo_path, check=True)
            subprocess.run(['git', 'config', 'user.email', 'user-email'], cwd=repo_path, check=True)

            # 메인화
            subprocess.run(['git', 'branch', '-M', 'main'], cwd=repo_path, check=True)

            # 기록조작
            commit_date = current_date.strftime('%a %b %d %H:%M:%S %Y %z')
            env = {
                'GIT_COMMITTER_DATE': commit_date,
                'GIT_AUTHOR_DATE': commit_date
            }

            # 커밋조지기
            subprocess.run(['git', 'add', '.'], cwd=repo_path, check=True)
            subprocess.run(['git', 'commit', '--date', commit_date, '-m', f'Commit for {current_date} - Part {commit_num}'], cwd=repo_path, env=env, check=True)
        
        # 원격레포있으면지워버리기
        subprocess.run(['git', 'remote', 'remove', 'origin'], cwd=repo_path, stderr=subprocess.PIPE, check=False)
        
        # 원격레포없으면만들기
        remote_url = f'https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git'
        subprocess.run(['git', 'remote', 'add', 'origin', remote_url], cwd=repo_path, check=True)
        
        # 원격레포에커밋푸시
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=repo_path, check=True)
        
        # 기록조작
        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    create_github_repo()
    create_commits()
