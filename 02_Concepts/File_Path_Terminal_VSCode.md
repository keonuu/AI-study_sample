# 파일 경로, 터미널, VS Code, 실행 위치

Tags: `PowerShell`, `Path`, `VS Code`, `WSL`, `Beginner`

## Summary

개발에서 명령어는 항상 현재 작업 위치를 기준으로 실행된다. 상대 경로는 현재 위치에 따라 의미가 달라지고, 절대 경로는 현재 위치와 상관없이 같은 파일을 가리킨다. VS Code에서 폴더를 열었더라도 터미널의 현재 위치를 확인해야 하며, Windows와 Ubuntu/WSL은 같은 파일도 경로 표현 방식이 다르다.

## File And Folder

- 파일: 하나의 문서, 코드, 데이터.
- 폴더: 파일과 다른 폴더를 담는 상자.

예시:

```text
F:\MyDesktop\AI_30Day_MasterPlan
├── 00_MasterPlan.md
├── 01_Daily
│   └── Day03.md
└── 02_Concepts
```

## Absolute Path And Relative Path

절대 경로는 처음부터 끝까지 모두 쓴 주소다.

```text
F:\MyDesktop\AI_30Day_MasterPlan\01_Daily\Day03.md
```

상대 경로는 현재 작업 위치를 기준으로 쓴 주소다.

현재 위치가 다음이면:

```text
F:\MyDesktop\AI_30Day_MasterPlan
```

같은 파일을 이렇게 부를 수 있다.

```text
01_Daily\Day03.md
```

## PowerShell Commands

현재 위치 확인:

```powershell
Get-Location
```

프로젝트 폴더로 이동:

```powershell
Set-Location F:\MyDesktop\AI_30Day_MasterPlan
```

파일 내용 출력:

```powershell
Get-Content 01_Daily\Day03.md
```

## Why Current Location Matters

현재 위치가 다음이면:

```text
C:\Users\un5567
```

이 명령어는 실패할 수 있다.

```powershell
Get-Content 01_Daily\Day03.md
```

PowerShell은 다음 파일을 찾으려고 하기 때문이다.

```text
C:\Users\un5567\01_Daily\Day03.md
```

그러나 실제 파일은 여기에 있다.

```text
F:\MyDesktop\AI_30Day_MasterPlan\01_Daily\Day03.md
```

## Windows And WSL Paths

Windows PowerShell:

```text
F:\MyDesktop\AI_30Day_MasterPlan
```

Ubuntu/WSL:

```text
/mnt/f/MyDesktop/AI_30Day_MasterPlan
```

변환 규칙:

```text
C:\  ->  /mnt/c/
F:\  ->  /mnt/f/
```

## Core Habit

명령어를 실행하기 전에 항상 확인한다.

1. 나는 지금 어느 폴더에 있는가?
2. 이 명령어는 어느 폴더에서 실행해야 하는가?
3. 이 명령어가 읽거나 수정할 파일은 어디에 있는가?

