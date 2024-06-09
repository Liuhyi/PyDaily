from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
import os


def application(environ, start_response):
    # 设置默认的请求/响应环境
    setup_testing_defaults(environ)

    # 获取请求的路径
    path = environ['PATH_INFO']
    # 路由逻辑
    if path == '/':
        response_body = home_page()
    elif path == '/hello':
        response_body = hello_page()
    elif path.startswith('/static/'):
        response_body, content_type = serve_static(path)
    else:
        response_body = not_found_page()

    # 构建响应头
    status = '200 OK' if path in ['/', '/hello'] or path.startswith('/static/') else '404 Not Found'
    headers = [('Content-Type', content_type if path.startswith('/static/') else 'text/html; charset=utf-8')]

    # 发送响应头
    start_response(status, headers)

    # 返回响应体
    return [response_body.encode('utf-8')]


def home_page():
    return '''
    <html>
    <head><title>Home Page</title></head>
    <body>
        <h1>Welcome to the Home Page</h1>
        <p><a href="/hello">Say Hello</a></p>
        <p><a href="/static/test.txt">View Static File</a></p>
    </body>
    </html>
    '''


def hello_page():
    return '''
    <html>
    <head><title>Hello Page</title></head>
    <body>
        <h1>Hello, World!</h1>
        <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''


def not_found_page():
    return '''
    <html>
    <head><title>404 Not Found</title></head>
    <body>
        <h1>404 Not Found</h1>
        <p>The requested page was not found on the server.</p>
        <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''


def serve_static(path):
    # 获取静态文件路径
    file_path = '.' + path
    if not os.path.isfile(file_path):
        return not_found_page(), 'text/html; charset=utf-8'

    # 读取文件内容
    with open(file_path, 'rb') as file:
        content = file.read()

    # 设置内容类型
    content_type = 'text/plain'
    if file_path.endswith('.html'):
        content_type = 'text/html'
    elif file_path.endswith('.css'):
        content_type = 'text/css'
    elif file_path.endswith('.js'):
        content_type = 'application/javascript'

    return content.decode('utf-8'), content_type


if __name__ == '__main__':
    port = 8000
    httpd = make_server('', port, application)
    print(f"Serving on port {port}...")
    httpd.serve_forever()
