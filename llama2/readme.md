# 트랜스포머(Transformer) 모델 프로젝트

## 트랜스포머란?
트랜스포머는 2017년 구글이 발표한 "Attention is All You Need" 논문에서 소개된 혁신적인 딥러닝 아키텍처입니다. 자연어 처리(NLP) 분야에서 획기적인 성능 향상을 이끌어낸 모델입니다.

### 주요 특징
- **셀프 어텐션(Self-Attention)**: 입력 시퀀스의 모든 단어들 간의 관계를 고려
- **병렬 처리**: RNN과 달리 병렬 처리가 가능하여 학습 속도가 빠름
- **위치 인코딩**: 순서 정보를 보존하기 위한 위치 정보 인코딩

### 대표적인 트랜스포머 기반 모델들
- GPT (Generative Pre-trained Transformer)
- BERT (Bidirectional Encoder Representations from Transformers)
- T5 (Text-to-Text Transfer Transformer)

## 이 프로젝트에 대하여
이 프로젝트는 OpenAI의 GPT 모델을 활용한 대화형 AI 시스템을 구현합니다.

### 주요 기능
- 대화형 인터페이스 제공
- 대화 내용 저장

### 설치 방법
- pip install openai 

### 사용 방법
1. `.env` 파일에 OpenAI API 키를 설정
2. `main.py` 실행
3. 프롬프트에 메시지 입력
4. 종료하려면 'exit' 입력

### 파일 구조
- `main.py`: 메인 실행 파일
- `conversation.txt`: 대화 내용 저장 파일
- `.env`: 환경 변수 설정 파일