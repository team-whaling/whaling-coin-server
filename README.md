# Whaling Coin server
## Stack
|Celery|RabbitMQ|Upbit
|:---:|:---:|:---:|
|<img src="./images/celery.png" width="50px" title="Celery" />|<img src="./images/rabbitmq.png" width="50px" title="RabbitMQ" />|<img src="./images/upbit.svg" width="50px" title="Upbit" />

# Feature
- 사용한 거래소 : [Upbit](https://upbit.com) 
- Upbit API Url : https://api.upbit.com 
- Upbit API Document : https://docs.upbit.com

## 주요 Task

### Coin

- 1분마다 Upbit에서 코인 가격을 받아와 업데이트(약 111개의 코인)
- S3 bucket에 코인 이미지 저장, 링크 저장해 두기

### Vote

- 투표 마감 기한 / 트래킹 기한이 되면 투표 상태 업데이트
- 코인 가격을 받아와 비교 연산을 실행하여 투표 정보를 업데이트
- 정답 여부에 따라서 유저에게 고래밥 지급 / 적중률 업데이트

### 개선해야 할 점
- 쿼리가 너무 복잡하게 되어 있다. 처음부터 객체 지향적으로 설계했다면 쿼리 수를 줄일 수 있었을 것
- 멀티 데이터베이스를 사용해도 되는 것인지에 대한 의문
- RabbitMQ에 대한 공부가 부족하여 기본 세팅으로만 되어 있는데, 보안적으로 괜찮은 지

### 직면했던 문제
- Celery가 돌고 있는 과정에서 EC2에 Deploy를 하면 서버가 터져버리는 문제 -> 프리티어 CPU 메모리 문제로 보여서 가상 메모리를 사용하여 해결
