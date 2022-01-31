# Whaling Coin server
---
## Stack
---
|Celery|Redis|Upbit
|:---:|:---:|:---:|
|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/aa576cba-e5b9-4851-b852-6e3c17b3e833/pngwing.com.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150811Z&X-Amz-Expires=86400&X-Amz-Signature=9703d4590d101a7055eb16c4bdf1ef00787c98e208e4a3d1d9527e42aa3ea838&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pngwing.com.png%22&x-id=GetObject" width="50px" title="Celery" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7eeac880-db91-4344-9d0e-9813f58189ea/redis_plain_wordmark_logo_icon_146367.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150821Z&X-Amz-Expires=86400&X-Amz-Signature=2aa58fc0812a51cf3ee17432e21592b5dd7c5d6ba4f61c609ef5f6383a90817c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22redis_plain_wordmark_logo_icon_146367.png%22&x-id=GetObject" width="50px" title="Redis" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3775bfa6-7637-43ab-b9b3-876adbfd85bd/upbit.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T151416Z&X-Amz-Expires=86400&X-Amz-Signature=50fa3ccda61aecca3011c98ab0b56692be8b4c6414999199fa3d54eff0bbc7c2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22upbit.svg%22&x-id=GetObject" width="50px" title="Upbit" />
## Feature
---
- 사용한 거래소 : [Upbit](https://upbit.com) 
- Upbit API Url : https://api.upbit.com 
- Upbit API Document : https://docs.upbit.com

### 주요 Task
---
- 1분마다 Upbit에서 코인 가격을 받아와 업데이트(약 121개의 코인)
- 메인 서버에 있는 투표를 받아와서 투표 마감 기한이 되면 투표를 닫아줌
- 투표가 설정한 기한이 되면 코인 가격을 비교하여 정답 여부를 업데이트



