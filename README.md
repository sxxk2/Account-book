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
9. [API 호출 테스트](#-api-호출-테스트)


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

<br>

## 👌🏻 API 호출 테스트

### User

<br>

#### 회원가입 성공 (201)
<img width="1006" alt="스크린샷 2023-02-06 오전 9 13 23" src="https://user-images.githubusercontent.com/83942213/216854787-7ebdf7b8-1027-4d04-a8d2-5fd9ee78aa9c.png">

<br>

#### 회원가입 실패 (400)
<img width="998" alt="스크린샷 2023-02-06 오전 9 19 25" src="https://user-images.githubusercontent.com/83942213/216855009-4ad26718-6c4e-404a-bf29-32dd2002243b.png">

- 이미 가입되어있는 이메일

<br>

#### 회원가입 실패 (400)
<img width="1001" alt="스크린샷 2023-02-06 오전 9 19 10" src="https://user-images.githubusercontent.com/83942213/216855148-faecdc86-59db-444f-8dbb-89c24d6ccb28.png">

- 비밀번호 유효성검사 통과 X (8~20자, 문자, 숫자, 기호의 조합)

<br>

#### 로그인 성공 (200)
<img width="998" alt="스크린샷 2023-02-06 오전 9 23 32" src="https://user-images.githubusercontent.com/83942213/216855312-ee65272e-f3f0-456b-bd9c-0875d0634ba7.png">

- aceess token과 refresh token 발급 후 리턴

<br>

#### 로그인 실패 (400)
<img width="996" alt="스크린샷 2023-02-06 오전 9 25 34" src="https://user-images.githubusercontent.com/83942213/216855570-2104b42c-876d-40fd-9e51-4f37208171cb.png">

- 잘못된 비밀번호 입력

<br>

#### 로그인 실패 (400)
<img width="999" alt="스크린샷 2023-02-06 오전 9 27 38" src="https://user-images.githubusercontent.com/83942213/216855687-e872e093-a565-4b97-be24-3e29748ebff0.png">

- 잘못된 이메일, 비밀번호 입력

<br>

#### 로그아웃 성공 (200)
<img width="999" alt="스크린샷 2023-02-06 오전 9 29 46" src="https://user-images.githubusercontent.com/83942213/216855894-f305f766-1d5e-4fe6-868b-a59f9bcb3825.png">

- 인증된 상태에서 정상적으로 발급받았던 refresh token과 함께 요청

<br>

#### 로그아웃 실패 (400)
<img width="997" alt="스크린샷 2023-02-06 오전 9 32 17" src="https://user-images.githubusercontent.com/83942213/216856094-d79ca381-7683-450f-9b72-a3634d83d636.png">

- 기존에 로그아웃 처리 되어 blacklisted 되어있는 refresh token으로 요청

<br>

#### 로그아웃 실패 (401)
<img width="1001" alt="스크린샷 2023-02-06 오전 9 31 22" src="https://user-images.githubusercontent.com/83942213/216856024-e258e63a-0fec-4f77-bdd4-20350a803145.png">

- 인증되지 않은 상태에서의 로그아웃 요청

<br>

#### access token 재발급 성공 (200)
<img width="997" alt="스크린샷 2023-02-06 오전 9 34 55" src="https://user-images.githubusercontent.com/83942213/216856254-3cfa8aa1-7b86-41b9-ad75-f9e59da01d65.png">

- 발급받았던 refresh token으로부터 access token 재발급

<br>

---

<br>

### Account_book

<br>

#### 가계부 생성 성공 (201)
<img width="996" alt="스크린샷 2023-02-06 오전 9 37 58" src="https://user-images.githubusercontent.com/83942213/216856465-5364fc1b-dbc9-4404-9d82-aea6447024a0.png">

<br>

#### 가계부 생성 실패 (400)
<img width="998" alt="스크린샷 2023-02-06 오전 9 39 19" src="https://user-images.githubusercontent.com/83942213/216856575-1a7927e0-2090-4b49-ada4-3b7d779820a4.png">

- 필수값 (title) 미입력

<br>

#### 가계부 목록 조회 성공 (200)
<img width="998" alt="스크린샷 2023-02-06 오전 9 44 10" src="https://user-images.githubusercontent.com/83942213/216857010-e1b1bab6-4d27-4fca-be79-ce7489660be8.png">

- 삭제되지 않은 (is_active=True) 가계부목록

<br>

#### 가계부 단건 조회 성공 (200)
<img width="1001" alt="스크린샷 2023-02-06 오전 9 45 17" src="https://user-images.githubusercontent.com/83942213/216857111-aa5fdea5-a608-4d9c-987a-3c709a5e58d0.png">

- 해당 유저가 생성한 가계부 조회

<br>

#### 가계부 단건 조회 실패 (403)
<img width="1005" alt="스크린샷 2023-02-06 오전 9 46 45" src="https://user-images.githubusercontent.com/83942213/216857257-b34febcf-34fa-47f0-8058-d377a57fe5a5.png">

- 다른 유저가 생성한 가계부 조회

<br>

#### 가계부 수정 성공 (200)
<img width="996" alt="스크린샷 2023-02-06 오전 9 48 04" src="https://user-images.githubusercontent.com/83942213/216857339-9df8e6a8-06f5-4c7f-874c-b16601a450f0.png">

- 가계부 수정과 함께 updated_at 컬럼 업데이트 

<br>

#### 가계부 삭제(soft delete) 성공 (200)
<img width="1000" alt="스크린샷 2023-02-06 오전 9 49 45" src="https://user-images.githubusercontent.com/83942213/216857479-fefaaace-f1f5-4b10-87bd-ad71f1263d66.png">

- is_active 컬럼과 delted_at 컬럼 수정

<br>

#### 삭제된 가계부 목록 조회 (200)
<img width="1001" alt="스크린샷 2023-02-06 오전 9 51 42" src="https://user-images.githubusercontent.com/83942213/216857611-dfce1c51-85bb-41e0-abad-f4abeeaeb55e.png">

<br>

#### 삭제된 가계부 복구 (200)
<img width="997" alt="스크린샷 2023-02-06 오전 9 53 56" src="https://user-images.githubusercontent.com/83942213/216858061-fb24f622-fe23-4b3f-b313-416bcc2dec72.png">

- is_active 컬럼 수정, deleted_at 컬럼 비움, updated_at 컬럼 복구시점으로 수정

<br>
#### 삭제된 가계부 완전삭제 성공 (204)
<img width="1004" alt="스크린샷 2023-02-06 오전 9 57 44" src="https://user-images.githubusercontent.com/83942213/216858443-2da3db97-ca2b-4956-9282-6bf612179ab3.png">

- 데이터베이스에서 완전 삭제

<br>

#### 삭제된 가계부 완전삭제 실패 (404)
<img width="995" alt="스크린샷 2023-02-06 오전 9 55 55" src="https://user-images.githubusercontent.com/83942213/216858296-1917307c-c2ed-4a15-9bb6-718f901c18f9.png">

- soft deleted 되지 않은 가계부의 완전 삭제 요청

<br>

#### 가계부 메모 생성 성공 (201)
<img width="1003" alt="스크린샷 2023-02-06 오전 9 59 49" src="https://user-images.githubusercontent.com/83942213/216858663-368cfcab-f3da-450a-9321-6942adc5d63d.png">

<br>

#### 가계부 메모 생성 실패 (400)
<img width="1000" alt="스크린샷 2023-02-06 오전 10 00 44" src="https://user-images.githubusercontent.com/83942213/216858767-a5a21860-5501-4438-9dec-080346619cc1.png">

- 필수 항목 미입력

<br>

#### 가계부 메모 생성 실패 (403)
<img width="1001" alt="스크린샷 2023-02-06 오전 10 01 30" src="https://user-images.githubusercontent.com/83942213/216858821-e9780ed2-9d23-4061-8628-5a87a8c2cd32.png">

- 다른 유저가 생성한 가계부에 메모 생성 요청

<br>

#### 가계부 메모 목록 조회 성공 (200)
<img width="997" alt="스크린샷 2023-02-06 오전 10 02 58" src="https://user-images.githubusercontent.com/83942213/216858947-866699e8-4019-44b6-9a8a-bf455b6db27f.png">

<br>

#### 가계부 메모 목록 조회 실패 (403)
<img width="997" alt="스크린샷 2023-02-06 오전 10 04 07" src="https://user-images.githubusercontent.com/83942213/216859016-9f681d96-d0c3-4731-8244-3acedd4efb2c.png">


- 다른유저의 가계부의 메모 목록 조회 요청 

<br>

#### 가계부 메모 단건 조회 성공 (200)
<img width="995" alt="스크린샷 2023-02-06 오전 10 05 31" src="https://user-images.githubusercontent.com/83942213/216859229-5867d515-0230-47ca-8d98-bdb72ff1a28c.png">

<br>

#### 가계부 메모 수정 성공 (200)
<img width="999" alt="스크린샷 2023-02-06 오전 10 06 38" src="https://user-images.githubusercontent.com/83942213/216859301-292bc365-e099-4d5d-8af0-afb56db9c1a1.png">

- 수정과 함께 updated_at 컬럼 수정

<br>

#### 가계부 메모 삭제(soft delete) 성공 (200)
<img width="994" alt="스크린샷 2023-02-06 오전 10 07 50" src="https://user-images.githubusercontent.com/83942213/216859384-77b0a82e-f5c8-4675-82ec-60e3ee0b18e8.png">

- is_actvie컬럼과 delted_at컬럼 수정

<br>

---

<br>

### 단축 URL

<br>

#### 단축 URL 생성 성공 (200)
<img width="996" alt="스크린샷 2023-02-06 오전 10 10 25" src="https://user-images.githubusercontent.com/83942213/216859629-1056d3e7-4674-41f5-8adb-48e02ae16df0.png">

- redis를 이용해 caching, 만료기간 900초 설정
- 단축URL : 원 URL 형태의 key:value로 저장

<br>

#### 단축 URL로부터 원 URL 요청 (200)
<img width="1000" alt="스크린샷 2023-02-06 오전 10 12 35" src="https://user-images.githubusercontent.com/83942213/216859807-12a2f1b6-c08b-47bb-b62a-8ac4ff9434fe.png">

- 캐싱 데이터베이스에서 단축URL의 key로 원래 URL을 찾아 리턴

