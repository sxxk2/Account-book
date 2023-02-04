# assignment


## 목차
<br>

1. [Summary](#-summary)
2. [사용 기술](#-사용-기술)
3. [ERD](#-erd)
4. [Task 관리](#-task-관리)
5. [API 명세서](#-api-명세서)
6. [브랜치 전략](#-브랜치-전략)
8. [컨벤션](#-코드-컨벤션)


<br>

## ✅ Summary
<br>

- 사용자가 본인의 소비내역을 기록/관리하는 가계부 서비스입니다.

<br>

- 인증은 JWT 토큰으로 이루어집니다.
- 회원가입, 로그인, 로그아웃 기능을 제공합니다.
- 로그아웃시 기존에 발급받은 refresh token을 blacklist에 담아 사용을 제한합니다.

<br>

- 인증된 사용자는 가계부를 생성, 수정, 삭제, 복구 할 수 있습니다.
- 인증된 사용자는 가계부에 연결되어있는 메모를 생성, 수정, 삭제 할 수 있습니다.
- 사용자가 공유를 원하는 자신의 가계부 내역을 손 쉽게 공유할 수 있도록 단축URL기능이 제공됩니다.
- 인증이 되지 않은 사용자에겐 접근을 제어합니다.

<br>

## 🛠 사용 기술

<div align="center">
<br>

<img src="https://img.shields.io/badge/Python-blue?style=plastic&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django Rest Framework-EE350F?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-00979D?style=plastic&logo=MySQL&logoColor=white"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=plastic&logo=Redis&logoColor=white"/>

<br>
<br>

<img src="https://img.shields.io/badge/Github Actions-2088FF?style=plastic&logo=github actions&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-F05032?style=plastic&logo=Git&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub-grey?style=plastic&logo=github&logoColor=181717"/>

</div>
<br>

<br>

## 💡 ERD

<img width="1011" alt="스크린샷 2023-02-04 오후 11 55 02" src="https://user-images.githubusercontent.com/83942213/216774785-f6980038-6aa5-445e-95df-2b7b2bc9dd56.png">


<br>

## 📜 API 명세서

<img width="680" alt="스크린샷 2023-02-04 오후 11 40 24" src="https://user-images.githubusercontent.com/83942213/216774781-76553e1a-5ee6-43a6-b218-fb9d38939856.png">

<br>

## 🔗 Task 관리

<img width="1078" alt="스크린샷 2023-02-04 오후 11 45 56" src="https://user-images.githubusercontent.com/83942213/216774748-b5632fd4-0867-4245-876c-1319d564bc50.png">


- Github의 <a href="https://github.com/sxxk2/assignment/issues" target="_blank">Issue</a> 와 
<a href="https://github.com/users/sxxk2/projects/6" target="_blank">Projects</a>를 사용합니다.
- issue 생성으로부터 개발을 시작하며 해당 기능을 개발 후 commit시 issue번호를 commit에 남깁니다.
- 명확한 라벨을 사용해 다른 작업자들도 한 눈에 보기 쉽게 구성했습니다.
 
<br>

## 🌱 브랜치 전략

- Github-flow를 사용합니다.
- main에서 파생된 feature 브랜치를 생성해 작업합니다.
- pull request를 통해 main에 병합합니다.
- pull reqeust template를 사용해 작업내용을 공유하고 호출테스트 사진을 첨부합니다.

<br>

## ✨🍰✨ 코드 컨벤션

- pre-commit
- github actions
- Formatter
  - isort
  - black
- Lint
  - flack8

<br>

### 💻 Local
<img width="662" alt="스크린샷 2022-08-19 오후 6 55 20" src="https://user-images.githubusercontent.com/83942213/185594792-dab3b933-9885-423a-a1b7-6f2c36d7af69.png">

- pre-commit 라이브러리를 통해 commit 시 자동으로 스테이징되어있는 코드에 대해 Formatter와 Linter를 실행합니다.
- 통과가 되지않는다면 커밋은 발생하지 않습니다.

<br>

### 🗄 Repository

<img width="1261" alt="스크린샷 2022-08-19 오후 7 16 54" src="https://user-images.githubusercontent.com/83942213/185597932-354cd857-330e-4f83-a372-2042b1035c64.png">

- push시 트리거가 되어 gitahub actions를 통해 코드 스타일을 체크합니다.
- pull reqeust상태에서 통과가 되지 않는다면 작업자들에게 알람을 줍니다.

<br>

## 💾 Pull reuqest 컨벤션

<img width="928" alt="스크린샷 2022-08-19 오후 7 26 25" src="https://user-images.githubusercontent.com/83942213/185613409-2402808f-e57b-4ed2-a49f-c15b36f06450.png">

- pull reuqest template가 .github 디렉토리에 저장되어있어, PR 생성시 자동으로 불러와집니다.
- 해당 PR에 대한 배경지식이 없거나 적은 동료 리뷰어에게 리뷰를 받는다는 전제로 객관적으로 항목들을 작성합니다.
- 작성한 API의 호출 테스트를 사진과 함께 첨부합니다.


