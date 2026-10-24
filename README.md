# 학교 축제 조사 수첩

중학교 2학년 인권 수업용 모바일 웹앱. 2~4명이 25분 동안 단서 6개를 조사하고 사연 3개를 연결한 뒤 해결 제안을 작성합니다.

## 실행

`dist` 디렉터리를 정적 HTTP 서버로 제공합니다. 설치·빌드·외부 API·데이터베이스가 필요하지 않습니다. 에셋과 글꼴은 로컬 파일로 제공됩니다. 기본 HTML/CSS/JavaScript로 구성되어 있습니다.

## 데이터

모든 상태는 `app.js`의 `state`에 메모리로만 유지됩니다. 브라우저 저장소·쿠키·서버 전송은 없습니다. 새로고침 시 초기화됩니다. 현재 '활동 마치기'는 결과 화면으로 이동하는 동작이며 서버 제출이 아닙니다.

후속 DB 연동 시 `complete()`에서 구성하는 `state.result`를 저장 경계로 사용합니다. 현재 데이터는 schemaVersion, activityId, person, evidenceIds, problem, proposal, investigatedClueIds, resolvedCases입니다. 실제 학생의 개인정보나 식별자는 수집하지 않습니다. 향후 저장 API와 동의·접근 정책은 별도 설계합니다.

## 검증

단서 잠금과 읽음 상태, 원문 재열기, 증거 2개 제한, 불완전 입력·오답·정답 피드백, 세 사연 완료 조건, 빈 해결 제안, 안전한 결과 문자열 렌더링, 제안 수정, 재시작 확인 및 초기화를 확인합니다.

## 에셋

캠퍼스 그림: 이 프로젝트를 위해 생성한 배경 이미지. 지명과 버튼은 HTML로 구현합니다.
Pretendard: SIL Open Font License. Phosphor Icons: MIT. 고지는 `dist/assets/`에 포함합니다.
