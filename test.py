# coding=gbk
"""
�������¶�ת��Ϊ�����¶�

Version: 0.1
Author: ���
"""
# f = float(input('�����뻪���¶�: '))
# c = (f - 32) / 1.8
# print('%.2f���϶� = %.2f���϶�' % (f,c))
# print(input('�����뻪���¶�: '))
# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1 ,s2)
# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# # sorted���������б������Ŀ��������޸Ĵ�����б�
# # ��������ƾ�Ӧ����sorted����һ�������ܲ�����������
# list3 = sorted(list1, reverse=True)
# # ͨ��key�ؼ��ֲ���ָ�������ַ������Ƚ������������Ĭ�ϵ���ĸ��˳��
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# # ���б���󷢳�������Ϣֱ�����б�����Ͻ�������
# list1.sort(reverse=True)
# print(list1)
#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         # yield a
#         print(a)
#
#
# def main():
#     # for val in fib(20):
#         print(fib(20))
#
#
# if __name__ == '__main__':
#     main()
# ����Ԫ��
# t = ('���', 38, True, '�Ĵ��ɶ�')
# print(t)
# # ��ȡԪ���е�Ԫ��
# print(t[0])
# print(t[3])
# # ����Ԫ���е�ֵ
# for member in t:
#     print(member)
# # ���¸�Ԫ�鸳ֵ
# # t[0] = '����'  # TypeError
# # ����t�����������µ�Ԫ��ԭ����Ԫ�齫����������
# t = ('����', 20, True, '��������')
# print(t)
# # ��Ԫ��ת�����б�
# person = list(t)
# print(person)
# # �б��ǿ����޸�����Ԫ�ص�
# person[0] = '��С��'
# person[1] = 25
# print(person)
# # ���б�ת����Ԫ��
# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)
# �������ϵ��������﷨
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# �������ϵĹ������﷨(������󲿷ֻ������ϸ����)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# �������ϵ��Ƶ�ʽ�﷨(�Ƶ�ʽҲ���������Ƶ�����)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)
# ���ϵĽ���������������ԳƲ�����
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# �ж��Ӽ��ͳ���
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))