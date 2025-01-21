'''
@author: zhegu
@version: 2.0
'''

import re
from requests import head, get, RequestException

def get_file_size(url):
    """获取文件大小"""
    try:
        response = head(url, allow_redirects=True)
        response.raise_for_status()
        return int(response.headers.get('Content-Length', 0))
    except RequestException as e:
        print(f"获取文件大小时发生错误: {e}")
        return 0

def download_chunk(url, start, end):
    """下载文件的指定分段"""
    headers = {'Range': f'bytes={start}-{end}'}
    try:
        response = get(url, headers=headers, stream=True, timeout=10)
        response.raise_for_status()
        if response.status_code == 206:
            print(f"下载分段 {start}-{end} 成功！")
            return response.content
        else:
            print(f"下载分段 {start}-{end} 失败，状态码: {response.status_code}")
            return None
    except RequestException as e:
        print(f"下载分段 {start}-{end} 时发生错误: {e}")
        return None

def download_file(url, file_name):
    """下载整个文件"""
    file_size = get_file_size(url)
    if file_size == 0:
        print("无法获取文件大小，下载终止。")
        return

    chunk_size = 1024 * 100  # 100 KB
    chunks = []

    for start in range(0, file_size, chunk_size):
        end = min(start + chunk_size - 1, file_size - 1)
        chunk = download_chunk(url, start, end)
        if chunk is None:
            break
        chunks.append(chunk)

    # 合并所有分段
    with open(file_name + '.pdf', 'wb') as f:
        for chunk in chunks:
            f.write(chunk)

    print("PDF 文件下载完成！")

def validate_filename(filename):
    """验证文件名是否合法"""
    if not filename:
        print("文件名不能为空。")
        return False
    # 使用正则表达式验证文件名
    if re.search(r'[\\/*?:"<>|]', filename):
        print("文件名包含非法字符。")
        return False
    return True

def main():
    print('''
用于下载 GM/T标准，理论上只要网页中存在类似URL都可以下载（未测试），使用请看说明文档
    ''')
    while True:
        url = input("请输入URL(输入q退出):").strip()
        if url.lower() == 'q':
            break
        file_name = input("请输入文件名（不带.pdf）:").strip()
        if not validate_filename(file_name):
            continue

        download_file(url, file_name)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"发生了另一个异常: {e}")
    # 在程序结束时，提示用户按任意键继续
    input("按任意键退出...")
