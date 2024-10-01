# Instructions: Please run code and follow the prompts that match the inputs
# provided to us on the assessment guidelines, answer for 3 tickets to the first prompt

class Ticketing_system:
    ticket_number = 2000  # Ticket numbers will start from 2000
    tickets_submitted = 0  # For counter display, these numbers will go up and down as the program is run.
    tickets_resolved = 0
    tickets_open = 0
    tickets_reopened = 0

    def __init__(self):

        self.ticket_numbers = []  # I have created many variables as empty arrays
        # need to make lists of the inputs i recieve i.e. names ect to print them on the tickets
        self.staffID_log = []
        self.ticket_creators = []
        self.email_log = []
        self.descriptions_log = []
        self.response_log = []
        self.ticket_status = []
        self.new_response_log = []

    def staffid_check(self):

        self.staffID = input("Please enter your Staff ID number: ")  # Asking for staff ID number
        staff_members = ['48356', '84529', '24894', '935449', '13632', '03633', '64932', '79451', '39456',
                         '52468']  # existing/valid staff ID numbers

        if self.staffID in staff_members:  # checking if the input of staff ID number is in the array above

            Ticketing_system.tickets_submitted += 1  # Adding these to counter as we have just opened a ticket.
            Ticketing_system.tickets_open += 1
            Ticketing_system.ticket_number += 1  # Assigning the ticket number adding 1 from the previous one assigned (it will start at number 2001)

            self.staffID_log.append(self.staffID)  # Appending staff ID to array
            self.ticket_numbers.append(Ticketing_system.ticket_number)  # Appending ticket number to array

            self.ticket_creator = input("Please enter your name: ")
            self.ticket_creators.append(self.ticket_creator)

            self.email = input(
                "Please enter your contact email: ")  # All of these are inputs asking for name, email and a description of the issue
            self.email_log.append(
                self.email)  # then appending it to the assigned lists in the initialisation function above.

            self.description = input("Please describe the issue you are needing help with: ")

            if "password" in self.description.lower() and "change" in self.description.lower():  # Checking if the response to input self.description contains words "password" and "change" in it while also converting to lower case
                new_password = ''.join([self.staffID[:2], self.ticket_creator[:3]])  # Creating a new password for the input that passed the if statement concatenating self.staffID first 2 values and self.ticket_creators first 3 values this will also turn it in to a string
                self.response = f"New password issued; your new password is; {new_password}"  # Will print new password in the ticket output
                self.response_log.append(self.response)  # Appending the response to the self.response_log array

                status = f"Closed"
                self.ticket_status.append(status)  # Updating/appending status as "Closed"

                self.descriptions_log.append(
                    self.description)  # Updating description and adding the bellow to the counter
                Ticketing_system.tickets_resolved += 1
                Ticketing_system.tickets_open -= 1
            else:
                r = f"Not yet provided. "  # Response updated to "Not provided yet"
                self.response_log.append(r)

                status = f"Open"  # Updating/appending status as "Open"
                self.ticket_status.append(status)

                self.descriptions_log.append(self.description)  # Updating description


        else:
            print("Not a valid Staff ID")  # If staff ID number was not in the staff_members array print this

    def all_tickets(self, ticket_number):  # Introducing a new variable which is the ticket numbers

        print("Ticket Number: ", self.ticket_numbers[ticket_number])  # Printing the ticket details from their arrays
        print("Staff ID: ", self.staffID_log[ticket_number])
        print("Ticket Creator: ", self.ticket_creators[ticket_number])
        print("Email Address: ", self.email_log[ticket_number])
        print("Description: ", self.descriptions_log[ticket_number])
        print("Response: ", self.response_log[ticket_number])
        print("Ticket Status: ", self.ticket_status[ticket_number])

    def reply(self):  # Ticket response method

        x = input("Would you like to reply to any tickets? ")  # Asking for input if user wants to respond now
        if x.lower() == "yes":  # If input is "Yes"
            ticket_number = int(
                input("Which ticket number would you like to respond to? "))  # Ask for ticket user wants to reply to

            if ticket_number in self.ticket_numbers:  # Checks if ticket number exists in the array
                reply = input("Please respond to this issue: ")  # If it is then asks for a response
                index_num = self.ticket_numbers.index(
                    ticket_number)  # will search through the array to find the index number of the ticket number provided
                self.response_log[index_num] = reply  # Appending/replacing the response to the self.response_log array
                self.ticket_status[index_num] = "Closed"  # Updating/appending status as "Closed"
                Ticketing_system.tickets_resolved += 1  # Updating counter
                Ticketing_system.tickets_open -= 1
            else:
                print(
                    "Ticket number does not exist.")  # If the ticket number provided is not in the list this will print

    def count_display(self):  # Counter method to display the following statistics

        print("Tickets submitted: ", self.tickets_submitted)
        print("Tickets resolved: ", self.tickets_resolved)
        print("Tickets open: ", self.tickets_open)
        print("Tickets re-opened: ", self.tickets_reopened)

    def new_tickets(
            self):  # To display the details of tickets after alterations (responses), taking out any tickets that were automatic password updates.

        for i in range(
                len(self.ticket_numbers)):  # Iterating through the range that is the length of ticket numbers array

            if "password" in self.descriptions_log[i].lower() and "change" in self.descriptions_log[
                i].lower():  # If it is a password change ticket
                pass  # It will pass and not re-print
            else:
                print("Ticket Number: ",
                      self.ticket_numbers[i])  # Printing the remaining tickets and their updated responses
                print("Ticket Creator: ", self.ticket_creators[i])
                print("Staff ID: ", self.staffID_log[i])
                print("Email Address: ", self.email_log[i])
                print("Description: ", self.descriptions_log[i])
                print("Response: ", self.response_log[i])
                print("Ticket Status: ", self.ticket_status[i])

    def reopening(self):  # Method for re-opening a ticket

        i = input("Would you like to re-open a ticket? ")  # Asking for input if user would like to re-open a ticket.
        if i.lower() == "yes":  # If response is yes then provide the number and carry out the below if statement
            ticket_num = int(input(
                "Please provide ticket number: "))  # Will turn the input into an intiger to use for finding in the index list

            if ticket_num in self.ticket_numbers:  # If the number provided is in our list of tickets
                Ticketing_system.tickets_reopened += 1  # Number of re-opened tickets will go up by 1
                Ticketing_system.tickets_resolved -= 1  # Number of resolved tickets will go down by 1
                index_num = self.ticket_numbers.index(
                    ticket_num)  # Updating/replacing the chosen ticket numbers status to re-opened
                self.ticket_status[index_num] = "Re-opened"
            else:
                pass  # if input was "no" we will simply pass this method


t = Ticketing_system()  # Assigning class to t

number_of_tickets = int(
    input("How many tickets are being made today? "))  # Fist inout to determine how many tickets will be created
for i in range(
        number_of_tickets):  # Calling the staffid_check function as many times as the user has input (how many tickets they're making)
    t.staffid_check()

t.count_display()  # Displaying the counter statistics after tickets are made.

for i in range(number_of_tickets):  # Calling the all_tickets function and iterating through.
    t.all_tickets(i)  # as many times as the tickets the user wants printing tickets accordingly.

t.reply()  # Calling reply method to update tickets

t.count_display()  # Displaying the counter statistics after tickets are updated with replies.
t.reopening()  # Calling function for re-opening tickets

t.count_display()  # Displaying the counter statistics after any tickets re-opened.
t.new_tickets()  # Calling function to print updated tickets