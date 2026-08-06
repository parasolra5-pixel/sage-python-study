# VS Code Compact Folder 문제

## 증상

폴더가 tools\old\ 로 한 줄 표시됨

## 원인

VS Code Explorer Compact Folders 설정

## 해결

explorer.compactFolders = false

방법 1 설정에서 찾기
VS Code 왼쪽 아래 ⚙️ 톱니바퀴
Settings(설정) 클릭
검색창에:
compact folders

입력

나오는:
Explorer: Compact Folders

체크를 끄면 됩니다

방법 2 settings.json에서 직접 변경
Ctrl + Shift + P
입력:
Preferences: Open User Settings (JSON)

선택

열린 파일에 아래 추가:
"explorer.compactFolders": false

예:

{
"explorer.compactFolders": false
}

저장하면 탐색기가:

변경 전:

tools\old\

변경 후:

tools
└─old

처럼 보입니다.
