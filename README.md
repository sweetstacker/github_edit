---

# GitHub Edit Repository

## Description
This repository demonstrates a Python script for creating a GitHub repository and generating daily commits with unique content. The script sets up a new GitHub repository, initializes a local Git repository, and creates commits with specified dates.

## Features
- Creates a GitHub repository.
- Generates daily commits with unique file content.
- Configures Git settings and pushes commits to the remote repository.

## Prerequisites
- Python 3.x
- `requests` library
- Git installed on your system
- GitHub personal access token with repository creation permissions

## Usage
1. Update the following variables in the script:
    - `GITHUB_TOKEN`: Your GitHub personal access token.
    - `REPO_NAME`: The name of the repository you want to create.
    - `GITHUB_USERNAME`: Your GitHub username.
    - `subprocess.run(['git', 'config', 'user.name', 'username'], cwd=repo_path, check=True)`: Enter your GitHub username in the username field.
    - `subprocess.run(['git', 'config', 'user.email', 'user-email'], cwd=repo_path, check=True)`: Enter your GitHub email in the user-email field.

2. Run the script to create the repository and generate daily commits.

```bash
python githubjojak.py
```

## License
This project is licensed under the Affero GNU General Public License 3.0 - see the [LICENSE](LICENSE) file for details.

---

# GitHub Edit Repository

## 설명
이 레포지토리는 GitHub 레포지토리를 생성하고 매일 커밋을 생성하는 파이썬 스크립트를 보여줍니다. 이 스크립트는 새로운 GitHub 레포지토리를 설정하고, 로컬 Git 레포지토리를 초기화하며, 지정된 날짜로 커밋을 생성합니다.

## 기능
- GitHub 레포지토리 생성
- 고유한 파일 내용을 가진 매일 커밋 생성
- Git 설정 구성 및 원격 레포지토리에 커밋 푸시

## 사전 요구 사항
- Python 3.x
- `requests` 라이브러리
- 시스템에 Git 설치
- 레포지토리 생성 권한이 있는 GitHub 개인 액세스 토큰

## 사용법
1. 스크립트에서 다음 변수를 업데이트합니다:
    - `GITHUB_TOKEN`: GitHub 개인 액세스 토큰
    - `REPO_NAME`: 생성할 레포지토리 이름
    - `GITHUB_USERNAME`: GitHub 사용자 이름
    - `subprocess.run(['git', 'config', 'user.name', 'username'], cwd=repo_path, check=True)`: username란에 GitHub 사용자 이름
    - `subprocess.run(['git', 'config', 'user.email', 'user-email'], cwd=repo_path, check=True)`: user-email란에 GitHub mail기입

2. 스크립트를 실행하여 레포지토리를 생성하고 매일 커밋을 생성합니다.

```bash
python githubjojak.py
```

## 라이센스
이 프로젝트는 Affero GNU General Public License 3.0에 따라 라이센스가 부여됩니다 - 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---
