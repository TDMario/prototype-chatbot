# run_frontend.py

from livereload import Server

server = Server()
server.watch('frontend/index.html')
server.watch('frontend/css/style.css')
server.watch('frontend/js/main.js')
server.serve(root='frontend', port=5500)