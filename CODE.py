class Stack:
    """
    Класс, реализующий структуру данных СТЕК
    """

    def __init__(self):
        self.__items = []  # внутреннее хранилище стека

    def _is_full(self) -> bool:
        """
        Внутренний метод: проверяет, заполнен ли стек
        """
        return len(self.__items) >= 100

    def push(self, n: int) -> str:
        """
        Добавляет элемент в стек
        """
        if self._is_full():
            return "Ошибка: стек переполнен"
        self.__items.append(n)
        return "ok"

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент
        """
        return self.__items.pop()

    def back(self) -> int:
        """
        Возвращает верхний элемент без удаления
        """
        return self.__items[-1]

    def size(self) -> int:
        """
        Возвращает количество элементов в стеке
        """
        return len(self.__items)

    def clear(self) -> str:
        """
        Очищает стек
        """
        self.__items.clear()
        return "ok"


def main() -> None:
    """
    Основная функция обработки пользовательских команд
    """
    stack = Stack()
    print("push n — добавить n в стек → вывести ok")
    print("pop — удалить последний элемент → вывести его")
    print("back — показать последний элемент (не удаляя)")
    print("size — вывести количество элементов")
    print("clear — очистить стек → вывести ok")
    print("exit — завершить программу → вывести bye")
    print("Введите команды:")
    print()

    while True:
        try:
            command = input().strip()

            if command.startswith("push "):
                _, value = command.split()
                print(stack.push(int(value)))

            elif command == "pop":
                print(stack.pop())

            elif command == "back":
                print(stack.back())

            elif command == "size":
                print(stack.size())

            elif command == "clear":
                print(stack.clear())

            elif command == "exit":
                print("bye")
                break

            else:
                print("Неизвестная команда")

        except ValueError:
            print("Ошибка: ожидалось целое число")

        except IndexError:
            print("Ошибка: стек пуст")

        except KeyboardInterrupt:
            print("\nПрограмма завершена вручную.")
            break

        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
