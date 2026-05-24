# 1. HTTP 내용 정리
## 1-1. HTTP란?
**HTTP(HyperText Transfer Protocol)**는 웹에서 클라이언트(브라우저, 앱)와 서버가 데이터를 주고받기 위한 약속(프로토콜)이다. 손님(클라이언트)이 종업원(서버)에게 정해진 말투로 주문하고, 서버가 정해진 형식으로 답하는 규칙이라고 보면 된다.
특징:

- 비연결성(Connectionless): 요청-응답이 끝나면 연결을 끊는다.
- 무상태(Stateless): 서버는 이전 요청을 기억하지 않는다. 그래서 로그인 상태 유지를 위해 쿠키, 세션, 토큰(JWT)을 따로 쓴다.
- 요청(Request) - 응답(Response) 구조: 클라이언트가 요청하면 서버가 반드시 응답한다.

## 1-2. HTTP 요청 구조
|이름|예시|내용|
|-----------------|------------------------------|-------------------------------|
|시작줄(Start Line)|POST /posts HTTP/1.1 |요청이나 응답의 상태를 나타내는 첫번째 줄|
|헤더(HTTP Headers)|Host: example.com|메시지 바디를 요약하는 헤더들의 집합|
|빈 줄(Empty line)|    |헤더와 본문을 구분하기 위해 존재하는 빈 줄|
|본문(Body)|{ "title": "안녕", "content": "첫 글" }| 데이터나 문서 등 실제 내용이 포함되며 HTML 문서, JSON 데이터 등이 본문에 담길 수 있음|

## 1-3. HTTP 메서드 (CRUD와 매핑)
|메서드|의미|CRUD|예시|
|----|-------|-----|-------|
|GET|자원 조회|Read|게시글 목록 보기|
|POST|자원 생성|Create|새 글 작성|
|PUT|자원 전체 수정|Update|글 통째로 교체|
|PATCH|자원 일부 수정|Update|제목만 수정|
|DELETE|자원 삭제|Delete|글 삭제|

## 1-4. HTTP 상태 코드
|코드 대역|의미|대표 예시|
|----|-------|------------|
|1xx|정보성|100 Continue|
|2xx|성공|200 OK, 201 Created, 204 No Content|
|3xx|리다이렉션|301 Moved Permanently, 304 Not Modified|
|4xx|클라이언트 오류|400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found|
|5xx|서버 오류|500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable|

## 1-5. 자주 쓰이는 헤더
- Content-Type: 보내는 데이터 형식 (예: application/json)
- Authorization: 인증 토큰
- Accept: 받고 싶은 응답 형식
- User-Agent: 클라이언트 정보 (브라우저 종류 등)

## 1-6. HTTPS
HTTP에 SSL/TLS 암호화를 추가한 것. 통신 내용을 도청·변조하지 못하게 한다. 요즘 서비스는 사실상 필수.
