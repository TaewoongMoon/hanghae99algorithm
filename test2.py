# input = [3,5,6,1,2,4]
# def find_max_num(): #첫번째 풀이방식
#     check_number = 0
#     for value in input:
#         if check_number < value:
#             check_number = value
#     return check_number
# print(find_max_num())

# def find_max_num(array): #2번째 풀이방식 (튜터)
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break;
#             else:
#                 return num

#2 최빈값 ASCII코드를 활용하여 찾아보기
# def find_alphabet_occurrence_array(string):
#     alphabet_occurrence_array = [0] * 26

#     return alphabet_occurrence_array


# Big-O and Big Omega 점근 표기법 문제
# input = [3,5,6,1,2,4]
# def is_number_exist(number, array):
#     for element in array: #n 만큼의 연산량
#         if number == element: #1번의 연산
#             return True
#     return False

#알고리즘 문제
# input = [3,4,5,6,7]
# max_result = 0
# def find_max_plus_or_multiply(array):
#     multiply_sum = 0
#     for number in array:
#         if number <= 1 or multiply_sum <=1:
#             multiply_sum += number
#         else:
#             multiply_sum *= number
#     return multiply_sum

# print(find_max_plus_or_multiply(input))

#알고리즘 문제2
# input = 'abadabac'
# def find_not_repeating_first_chracter(string):
#      for element in string: #O(N^2)
#          repeating_element = ''
#          for element_next in string:
#              if element == element_next:
#                  repeating_element += element_next
#          if repeating_element >= 2*element:
#              continue
#          else:
#              return element


#ASCII code를 이용한 알고리즘 2번 문제풀이
# def find_not_repeating_frist_character2(string):
#     alphabet_occurrence_array = [0] *26
#     for char in string:
#         if not char.isalpha():
#             continue
#         arr_index = ord[char] - ord['a']
#         alphabet_occurrence_array[arr_index] += 1




# print('세 정수의 최댓값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b값을 선택하세요:'))
# c = int(input('정수 c값을 선택하세요.:'))




# maximum_ = a
# if b > maximum_:
#     maximum =b
# if c > maximum_:
#     maximum =c
# print(f'최댓값은 {maximum}입니다.')

# # 음수가 나올경우 계속해서 문구를 뛰워주는 알고리즘
# while True:
#     n=int(input('n의값을 지정해주세요:'))
#     if n >0:
#         break

# #직각 이등변 삼각형 만들기
# for i in range(n):
#     for j in range (i+1):
#         print('*', end='')

def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i ==0:
            return 0
    return x!=1

print(prime(13))