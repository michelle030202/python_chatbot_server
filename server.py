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
        """
        The function gets raw string, and tries to run the
        matching action function.
        """
        print("[INFO] Word to analyze: ", str_to_analyze)
        if str_to_analyze.startswith("ping"):
            return self.ping(str_to_analyze)

        elif str_to_analyze.startswith("solve"):
            print(self.solve(str_to_analyze))
            return self.solve(str_to_analyze)

        elif str_to_analyze.startswith("reverse"):
            return self.reversed(str_to_analyze)
        else:
            error = "[ERROR] Unknown analyze command for string: %s" % str_to_analyze
            print("%s" % error)
            return error

    def ping(self, str_to_analyze):
        """
        The function gets string that starts with 'ping', and
        returns the text after the word 'ping'
        """
        word_to_ping = str_to_analyze.replace('ping ', '', 1)  # Replace first occurrence of "ping "
        return word_to_ping

    def solve(self, str_to_analyze):
        """
        The function gets math equation to solve.
        The input needs to be as following 'solve num1 math_sign num2'.
        For example "solve 1 + 4" return 5
        """
        if len(str_to_analyze.split()) != 4:
            error = "[ERROR] The input string need to be as following 'solve num1 math_sign num2'"
            print("%s" % error)
            return error
        solve, num1, sign, num2 = str_to_analyze.split()

        try:
            num1, num2 = float(num1), float(num2)
        except:
            error = "[ERROR] num1 and num2 needs to be numbers."
            print("%s" % error)
            return error

        if sign == '+':
            return num1 + num2

        elif sign == '-':
            return num1 - num2

        elif sign in [':', '/']:
            try:
                return num1 / num2

            except ZeroDivisionError:
                error = "[ERROR] Can't divide by zero, try again"
                print("%s " % error)
                return error

        elif sign in ['*', 'x', 'X']:
            return num1 * num2

        else:
            error = "[ERROR] unknown math sign %s " % sign
            print("%s " % error)
            return error

    def reversed(self, str_to_analyze):
        """
        The function reverse the input string, e.g.
        "hello world" -> "dlrow olleh"
        """
        word_ro_reverse = str_to_analyze.replace('reverse ', '', 1)  # Replace first reverse word
        word_ro_reverse = word_ro_reverse[::-1]
        return word_ro_reverse


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


