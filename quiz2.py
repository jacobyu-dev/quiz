lines: list = []
f = open('data/quiz2.txt', mode='r')
# print(f.read())
for line in f.readlines():
  lines.append(line)
f.close()

# TODO: 
# 위 코드는 'data/quiz2.txt'의 텍스트를 줄 단위로 읽어들이는 코드입니다.
# 아래 조건에 맞추어 정답을 계산하세요.

# 조건 1. 
#  두번째 라인에서 마지막 라인까지의 숫자를 읽어들여
# 조건 2. 
#  직전 라인에서 계산된 최종 값에(첫번째 라인은 계산하지 않음) 
#   - 3의 배수면 곱하기
#   - 10의 배수면 빼기
#   - 소수면 나누기
#   - 그 외의 값은 더하기
#  를 한 결과 값(정답)을 'data/quiz2.txt'에 저장해 주세요.
#  조건 3, 
#   단, 정답은 결과 파일의 첫번째 줄에 위치해야 합니다.

# 제약 조건 
#   모듈 또는 라이브러리를 추가로 로드하지 않습니다. 
#   파이썬 코드 파일을 추가로 생성하지 않습니다. 
#   상단 코드는 하단의 코드로 결과를 확인할 수 있는 한 마음껏 수정하셔도 됩니다.

# {코드 작성 시작}

def IsPrimeNumber(n):
  # 2부터 (n - 1)까지의 모든 수를 확인
  for i in range(2, n):
      if n % i == 0:
          return False # 소수가 아님
  return True

answer = 0
lines = list(map(int, lines)) # 타입 변환

for i in range(1,len(lines)):
  if (lines[i])%3 == 0: #3의 배수
    answer += (lines[i-1] * lines[i])
  elif lines[i]%10 == 0:  #10의 배수
      answer += (lines[i-1] - lines[i])
  elif IsPrimeNumber(lines[i]) == True:  # 소수
      answer += (lines[i-1] / lines[i])
  else:  # 더하기
      answer += (lines[i-1] + lines[i])
print('answer : ', answer )


# 파일 읽고, 저장
lines = list(map(str, lines))
lines.insert(0, str(answer))
for k in range(len(lines)):
  lines[k] +='\n'

f = open('data/quiz2.txt', mode='w')
for j in lines:
  f.write(j)

# for line in f.readlines():
#   lines.append(line)
# lines.insert(0, str(answer))
# {코드 작성 완료}

f = open('data/quiz2.txt', mode='r')
print(f.read())
f.close()