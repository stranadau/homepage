# STRANA 홈페이지 (Hugo)

`main`에 push하면 GitHub Actions가 자동으로 빌드·배포합니다(`.github/workflows/pages.yml`).

## 자주 하는 업데이트
| 할 일 | 수정할 파일 |
|---|---|
| 소식 추가 (학회, 수상, 논문, 학위 등) | `data/news/`에 YAML 파일 1개 추가 |
| 논문 추가 | `data/publications.yaml` (journals / conferences / reports) |
| 구성원 변경, 졸업생 이동 | `data/members.yaml` |
| 학위논문 추가 | `data/theses.yaml` + 저장소 `theses/` 폴더에 PDF |
| 강의 (학기별) | `data/teaching.yaml` |
| 연구 주제와 대표 논문 | `data/research.yaml` |
| 진학 안내, 이력 | `content/ko/join`, `content/en/join`, `content/*/cv` |

소식 파일 예시 (`data/news/2026-10-15-ksce-award.yaml`):
```yaml
date: "2026-10-15"        # 일자를 모르면 "2026-10" 또는 "2026"
type: award               # conference | award | publication | talk | degree | member
title: {ko: "대한토목학회 우수논문발표상 수상 (홍길동)", en: "Best Presentation Award at KSCE (Gildong Hong)"}
body: {ko: "발표 제목 ...", en: "Title ..."}   # 선택
link: https://...                                # 선택
```

사진과 PDF는 저장소 최상위 `images/`, `theses/` 폴더를 그대로 사용합니다.

## 로컬 빌드
`./build.sh` → `public/` 생성 (이전 사이트는 `public/legacy/`에 포함)
