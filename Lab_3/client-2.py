import requests
import sys

class MovieClient:
    def __init__(self, server_ip):
        self.server_url = f"http://{server_ip}:8000"
        print(f"Подключаемся к серверу: {self.server_url}")
    
    def check_connection(self):
        try:
            response = requests.get(f"{self.server_url}/", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def show_all_movies(self):
        try:
            response = requests.get(f"{self.server_url}/movies", timeout=5)
            data = response.json()
            if "movies" in data:
                return data["movies"]
            return []
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            return []
    
    def get_movie(self, movie_id):
        try:
            response = requests.get(f"{self.server_url}/movies/{movie_id}", timeout=5)
            return response.json()
        except Exception as e:
            return {"error": f"Не удалось подключиться к серверу: {e}"}
    
    def add_movie(self, title, year, genre):
        try:
            movie_data = {
                "id": 0,
                "title": title,
                "year": year,
                "genre": genre
            }
            response = requests.post(f"{self.server_url}/movies", json=movie_data, timeout=5)
            return response.json()
        except Exception as e:
            return {"error": f"Не удалось добавить фильм: {e}"}
    
    def update_movie(self, movie_id, title, year, genre):
        try:
            movie_data = {
                "id": movie_id,
                "title": title,
                "year": year,
                "genre": genre
            }
            response = requests.put(f"{self.server_url}/movies/{movie_id}", json=movie_data, timeout=5)
            return response.json()
        except Exception as e:
            return {"error": f"Не удалось обновить фильм: {e}"}
    
    def delete_movie(self, movie_id):
        try:
            response = requests.delete(f"{self.server_url}/movies/{movie_id}", timeout=5)
            return response.json()
        except Exception as e:
            return {"error": f"Не удалось удалить фильм: {e}"}

def main():
    if len(sys.argv) < 2:
        print("Использование: python client.py <IP_адрес_сервера>")
        print("Пример: python client.py 192.168.1.100")
        return
    
    server_ip = sys.argv[1]
    client = MovieClient(server_ip)
    
    if not client.check_connection():
        print("Не удалось подключиться к серверу. Проверьте:")
        print("1. Правильность IP-адреса")
        print("2. Запущен ли сервер на порту 8000")
        print("3. Настройки firewall")
        return
    
    print("=== Клиент для управления фильмами ===")
    print("Успешное подключение к серверу!")
    
    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Найти фильм по ID")
        print("4. Обновить фильм")
        print("5. Удалить фильм")
        print("6. Выйти")
        
        choice = input("Ваш выбор (1-6): ")
        
        if choice == "1":
            movies = client.show_all_movies()
            if movies:
                print("\nСписок фильмов:")
                for movie in movies:
                    print(f"ID: {movie['id']}, {movie['title']} ({movie['year']}), жанр: {movie['genre']}")
            else:
                print("Фильмов нет в базе данных")
        
        elif choice == "2":
            title = input("Название фильма: ")
            try:
                year = int(input("Год выпуска: "))
            except:
                print("Год должен быть числом!")
                continue
            genre = input("Жанр: ")
            result = client.add_movie(title, year, genre)
            print(result)
        
        elif choice == "3":
            try:
                movie_id = int(input("ID фильма: "))
            except:
                print("ID должен быть числом!")
                continue
            movie = client.get_movie(movie_id)
            if "error" not in movie:
                print(f"Найден фильм: {movie['title']} ({movie['year']}), жанр: {movie['genre']}")
            else:
                print(movie["error"])
        
        elif choice == "4":
            try:
                movie_id = int(input("ID фильма для обновления: "))
            except:
                print("ID должен быть числом!")
                continue
            title = input("Новое название: ")
            try:
                year = int(input("Новый год выпуска: "))
            except:
                print("Год должен быть числом!")
                continue
            genre = input("Новый жанр: ")
            result = client.update_movie(movie_id, title, year, genre)
            print(result)
        
        elif choice == "5":
            try:
                movie_id = int(input("ID фильма для удаления: "))
            except:
                print("ID должен быть числом!")
                continue
            result = client.delete_movie(movie_id)
            print(result)
        
        elif choice == "6":
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()