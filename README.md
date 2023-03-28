# todo-manager

## 할일 매니저 토이 프로젝트
- 여러가지 할일을 칸반보드등으로 관리하는 프로그램
- 프로그램 설계서, 프로그램 ERD 추가
- Django rest framework 아키텍처(요건 생각좀)

### Back-End
[stack]
- Django Rest Framework
### 프로젝트 셋팅
#### 프로젝트 생성
```Bash
# 프로젝트 폴더 생성
> mkdir todo-manager-be
# 프로젝트 폴더 이용후 가상환경 생성(python3에 내장되어있는 venv로 가상환경 생성)
> python3 -m venv venv
# 프로젝트 구성(프로젝트 생성시 설정파일 담길 곳이라 폴더명 config로 생성 마지막 마침표 중요!! 해당 폴더에 생성되도록 하는것 아니면 같은 이름에 폳더 안쪽에 생성됨)
> django-admin startproject config .
```
#### 프로젝트 소스 github clone(https)
```Bash
> git clone "https://github.com/daeyoungshinme/todo-manager-be.git"
```

#### 프로젝트 서버 구동
```Bash
> python3 manage.py runserver
```

#### 프로젝트 API 개발 가이드
- API 모델 생성
  - 생성된 app model에 모델 설정
- API Serialize 생성
  - 설정한 모델에 json형식으로 시리얼라이저할 파일 생성 및 설정
- API View 생성
  - veiw 비지니스 로직 구현 및 앞에 생성한 모델과 시리얼라이즈를 이용해서 json형식의 response 리턴
- API URL 생성
  - 앞에서 구현한 view로 연동할 url구성후 view 호출
- API 리턴 확인
  - 브라우저에서 api 리턴 확인
- API 설계서 작성
- 추후 추가 구성
  - 배포구성
  - TDD구성
  - nginx, uWsgi 구성(설정 및 구성)
  - 비동기 처리1... python 내부적으로 처리
  - 비동기 처리2... RabbitMq + Celery 구성
  - 비동기 처리3... Radis + Celery 구성 
  - 비동기 처리4... kafka + Celery 구성
  - 스케줄러구성(CeleryBeat, Crontab)
  - 로그처리 elasticSearch + kibana 구성


