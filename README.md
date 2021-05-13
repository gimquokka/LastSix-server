# 개요

*Software Maestro* 12기 공공데이터 활용 해커톤 LastSix 팀 (고동천, 김진영, 함초롬, 박효진, 진유진, 이종아)의 의약 폐기물 처리 안내 사이트 *"약! 그냥 버리게?"* 웹 어플리케이션의 서버 프로젝트입니다.



# 기술 스택

```markdown
### 사용한 라이브러리 ###
- flask
- mongoDB
- pymongo
- python

### 활용한 공공데이터 목록 ###
1. 서울특별시_양천구_폐의약품_수거함위치
(https://data.go.kr/data/15074902/fileData.do)
2. 서울특별시 용산구_폐의약품 수거가능위치 현황 
(https://data.go.kr/data/15074891/fileData.do)
3. 서울특별시 동대문구_폐의약품 수거함 위치 현황 
(https://data.go.kr/data/15074660/fileData.do)
4. 서울특별시 광진구_폐의약품 수거함 및 수집 참여 약국 현황 
(https://data.go.kr/data/15075017/fileData.do)
5. 서울특별시 동작구_폐의약품 수거가능 약국현황 
(https://data.go.kr/data/15077702/fileData.do)
6. 서울특별시 강서구_폐의약품 수거 약국 현황 
(https://data.go.kr/data/15074907/fileData.do)
7. 서울특별시 은평구_폐의약품수거거점약국 
(https://data.go.kr/data/15077807/fileData.do)
8. 서울특별시 송파구_폐의약품 수거 참여 약국 현황 
(https://data.go.kr/data/15077652/fileData.do)
9. 서울특별시 서대문구_가정폐의약품 수거함 위치 
(https://data.go.kr/data/15074855/fileData.do)
10. 서울특별시 마포구_불용의약품수거함 
(https://data.go.kr/data/15074773/fileData.do)
11. 국립중앙의료원_전국 약국 정보 조회 서비스 
(https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000576)
```



# 프로젝트 구조

```python
├─ Readme.md
├─ modules
│  ├─ __init__.py     
│  └─ garbege.py (will replaced)
├─ routes.py
├─ wsgi.py  
└─ .gitignore
```

