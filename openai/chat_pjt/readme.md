# 🤖 Django OpenAI Chat Project

Django와 OpenAI API를 활용한 채팅 애플리케이션입니다.

## 🛠 기술 스택

- **Backend**: Django REST Framework
- **AI**: OpenAI GPT API
- **인증**: JWT (Simple JWT)
- **문서화**: drf-spectacular (Swagger/ReDoc)
- **캐싱**: Redis
- **모니터링**: Django Silk

## ⚙️ 주요 기능

### 1. 사용자 인증
- JWT 기반 인증 시스템
- 토큰 갱신 기능
- 사용자 회원가입/로그인

### 2. ChatGPT 대화
- OpenAI API 연동
- 실시간 채팅 응답
- 대화 내역 저장 및 조회

### 3. API 기능
- RESTful API 설계

## 🚀 시작하기

1. 환경 설정
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt
```

2. 환경변수 설정
```bash
# .env 파일 생성
OPENAI_API_KEY=your_api_key_here
DJANGO_SECRET_KEY=your_secret_key_here
```

3. 데이터베이스 설정
```bash
python manage.py migrate
```

4. 서버 실행
```bash
python manage.py runserver
```

## 📁 프로젝트 구조
```
chat_pjt/
├── accounts/         # 사용자 인증 관련
├── api_pjt/         # 프로젝트 설정
├── articles/        # 게시글 관련
├── chatgpt/         # OpenAI 채팅 관련
└── products/        # 상품 관련
```

## 🔍 API 문서
- Swagger UI: `/api/v1/schema/swagger-ui/`
- ReDoc: `/api/v1/schema/redoc/`

## 🔐 보안
- API 키는 환경변수로 관리
- JWT 기반 인증으로 보안 강화
- Redis를 통한 세션 관리

## 🛠 성능 모니터링
- Django Silk를 통한 API 성능 모니터링
- Redis 캐싱으로 응답 속도 최적화

## 📝 라이선스
This project is licensed under the MIT License

