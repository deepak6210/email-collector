"""Email Collector(this email collector take all the email's from my str and make a list of it
and store it i a separate file """
# Here we are using regular Expression module to search our email from my string
# you can update your string
my_str = ""
def find():
    import re
    my_email_list = re.findall(r'\w+@\S+\w', my_str)
    op = open("All_Gmail.txt","a")
    serial_no = 1
    for i in my_email_list:
        op.write(f"Email{serial_no}:{i}\n")
        serial_no = serial_no+1

if __name__ == '__main__':
    find()
    print("all the Gmails are collected in the file name All_Gmail.txt go and check out it")