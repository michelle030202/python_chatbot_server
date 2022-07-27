import socket
import threading


host = socket.gethostbyname(socket.gethostname())
port = 5050   # Port to listen on
FORMAT = 'utf-8'
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)
print("[INFO] Server is running...")


class Chatbot:
    """
    Chatbot's class contains set of actions to help the client.
    """
    def __init__(self):
        pass

    def analyze(self, str_to_analyze):
        first_word = str_to_analyze.split()[0]
        rest_of_word = str_to_analyze.replace(first_word + " ", '', 1)
        try:
            result = getattr(self, first_word)(rest_of_word)
            print(result)
            return result

        except:
            return "Igal type something else"

    def ping(self, str_to_analyze):
        """
        The function gets string that starts with 'ping', and
        returns the text after the word 'ping'
        """
        return str_to_analyze

    def solve(self, str_to_analyze):
        """
        The function gets math equation to solve.
        The input needs to be as following 'solve num1 math_sign num2'.
        For example "solve 1 + 4" return 5
        """
        try:
            result = eval(str_to_analyze)
        except Exception as e:
            return e
        return result

    def reverse(self, str_to_analyze):
        """
        The function reverse the input string, e.g.
        "hello world" -> "dlrow olleh"
        """
        word_reversed = str_to_analyze[::-1]
        return word_reversed


connected = True
while connected:
    def ping_back():
        conn, addr = serv.accept()
        inp = conn.recv(2048).decode()  # get input from client
        print("[INFO] Got input from user: %s " % inp)
        output = Chatbot().analyze(str(inp))
        print("[INFO] ChatBot's output: %s " % output)
        conn.send(str(output).encode(FORMAT))
        thread = threading.Thread(target=ping_back)
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    ping_back()


