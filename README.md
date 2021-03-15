# py_codesave
자동으로 정답을 맞춘 알고리즘 코드를 깃헙에 올려줍니다.

# 설치 방법
```python
pip install py-codesave==0.0.3
pip install py_codesave
```

# 사용방법
### 패키지 불러오기
```python
from py_codesave import main
```

### 도움
```python
main.help()
```

### 실행
```python
main.run('boj', '토큰값', 'repository이름')
# 예시 - 사이트는 'boj' 레포지토리의 이름은 'test'라면,
# main.run('boj', '토큰값', 'sawol/test')
```
