#Method Overriding
class ineuron:

    def student(self):

        print("Print the details of all the students")

    def achiever(self):

        print("Print the list of all achiever")

    def hall_of_fame(self):

        print("Print everyone from hall of fame")

class ineuron_vision(ineuron):

    def student(self):

        print("These are the filter students")

iv = ineuron_vision()
iv.student()