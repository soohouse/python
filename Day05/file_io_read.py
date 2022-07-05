
'''
* 파일 읽기 기능(read)

- 파일로부터 데이터를 읽어들일 때는 분량에 따라
적당한 메서드를 선택해서 사용합니다.

1. read(): 파일 전체를 통째로 읽어서 리턴.
2. readline(): 파일 데이터를 한 줄씩 읽어서 리턴.
3. readlines(): 파일 전체를 읽어서 한 줄씩 분리한 후에
리스트에 담아서 리턴.
'''
file_path = '/Users/dood/Desktop/java_web_JS/python/test/test.txt'

'''
try:
    f = open(file_path, 'r')
    text = f.read()
    print(text)
except:
    print('파일 로드 실패!')
finally:
    f.close()
'''

# readline() 메서드는 자동으로 \n을 기준으로 하여
# 데이터를 줄 단위로 읽어들이기 때문에 메모리 부담을 좀 더
# 줄일 수 있습니다.

'''
try:
    f = open(file_path, 'r')
    while True:
        text = f.readline()
        print(text)
        if len(text) == 0:
       # if '반복문' in text:
       #     break
    
    
except:
    print('파일 로드 실패!')
finally:
    f.close()
'''