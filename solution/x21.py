def solution(n, words):
  used_words = set( )   # ➊ 이미 사용한 단어를 저장하는 set
  prev_word = words[0][0]  # ➋ 이전 단어의 마지막 글자

  for i, word in enumerate(words):
    # ➌ 이미 사용한 단어거나 첫 글자가 이전 단어와 일치하지 않으면
    if word in used_words or word[0] != prev_word:
      # ➍ 탈락하는 사람의 번호와 차례를 반환
      return [(i % n) + 1, (i // n) + 1]
    used_words.add(word)  # ➎ 사용한 단어로 추가
    prev_word = word[-1]  # ➏ 이전 단어의 마지막 글자 업데이트
  return [0, 0]  # ➐ 모두 통과했을 경우 반환값
